"""Streamlit dashboard with a preliminary SEC score view and fictional UI demo."""

import csv
from html import escape

import pandas as pd
import plotly.graph_objects as go
import streamlit as st

from src.dashboard.mock_data import (
    DEMO_AREAS,
    DEMO_STAGES,
    FIRMS,
    compare_timeline,
    compare_use_cases,
    get_firms,
    get_use_cases,
    summarize_use_cases,
)
from src.dashboard.score_data import load_company_scores, validate_firm_labels
from src.dashboard.theme import (
    BODY_FONT,
    CHART_PALETTE,
    COLORS,
    HEADING_FONT,
    STAGE_COLORS,
    THEME_CSS,
)

st.set_page_config(
    page_title="AI Adoption Index | SEC Pilot",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown(THEME_CSS, unsafe_allow_html=True)


def chart_layout(title, y_title=None):
    return {
        "title": {
            "text": title,
            "x": 0,
            "xanchor": "left",
            "font": {"family": HEADING_FONT, "size": 18, "color": COLORS["structural"]},
        },
        "paper_bgcolor": "rgba(0,0,0,0)",
        "plot_bgcolor": COLORS["surface"],
        "font": {"family": BODY_FONT, "color": COLORS["text"]},
        "margin": {"l": 12, "r": 18, "t": 48, "b": 20},
        "xaxis": {"title": None, "showgrid": False, "linecolor": COLORS["border"]},
        "yaxis": {"title": y_title, "gridcolor": COLORS["border"], "zerolinecolor": COLORS["border"]},
        "legend": {"orientation": "h", "y": -0.22},
        "hovermode": "closest",
    }


def records_frame(records):
    return pd.DataFrame([
        {
            "Period": record["quarter"],
            "Illustrative use case": record["title"],
            "Example area": record["area"],
            "Demo stage": record["stage"],
        }
        for record in records
    ])


st.markdown('<div class="eyebrow">Financial services · research preview</div>', unsafe_allow_html=True)
st.title("AI Adoption Index | SEC pilot + envisioned demo")
st.write(
    "Explore preliminary annual scores calculated from SEC filing labels, then switch to a "
    "separate fictional walkthrough of an envisioned evidence-backed dashboard."
)
st.warning(
    "**TWO DISTINCT DATA TRACKS.** The SEC pilot tab shows preliminary scores calculated from "
    "SEC disclosure passages and AI-assisted v0 labels; these are not verified measures of "
    "firm-wide adoption. The envisioned tabs use fictional records, dates, categories, and "
    "stages for interface demonstration only. Never interpret those mock examples as company claims."
)

score_data = None
score_data_error = None
try:
    score_data = load_company_scores()
    validate_firm_labels(score_data, FIRMS)
except (OSError, ValueError, csv.Error) as exc:
    score_data_error = str(exc)

sectors = sorted({firm["sector"] for firm in FIRMS})
with st.sidebar:
    st.markdown("### Envisioned mockup filter")
    selected_sector = st.selectbox("Sector", ["All sectors", *sectors], index=0)
    sector_filter = None if selected_sector == "All sectors" else selected_sector
    sector_firms = get_firms(sector_filter)
    firm_labels = {firm["ticker"]: firm["company"] for firm in sector_firms}
    selected_ticker = st.selectbox(
        "Company", list(firm_labels), format_func=lambda ticker: firm_labels[ticker]
    )
    selected_firm = next(firm for firm in sector_firms if firm["ticker"] == selected_ticker)
    st.caption("This selector filters the fictional firm-story walkthrough only.")

scores_tab, story_tab, compare_tab, about_tab = st.tabs(
    ["SEC pilot scores", "Envisioned firm story", "Envisioned comparison", "About the data"]
)

with scores_tab:
    st.subheader("Preliminary SEC disclosure scores")
    st.write(
        "Each row is a company–fiscal-year score calculated from labeled SEC filing passages. "
        "These are disclosure-based pilot metrics, not a census of a firm's AI activity or a "
        "final adoption index."
    )
    st.warning(
        "**PRELIMINARY / AI-ASSISTED V0.** The current score file uses AI-assisted draft "
        "passage labels and the v0 scoring method. A score of 0 means no scored use was found "
        "in the available labeled disclosures; it does not establish that the firm does not use AI."
    )
    st.caption(
        "The score file contains annual observations. FY2026 is partial (source filings through "
        "June 30, 2026); Citi and Principal have no FY2023 score. Missing firm-years are shown "
        "as unavailable, never as zero. This file has no evidence IDs or citations, so this view "
        "does not provide passage-level drill-down."
    )

    if score_data_error:
        st.error(f"Could not load the SEC score file: {score_data_error}")
    elif score_data is not None:
        score_years = sorted({score.fiscal_year for score in score_data})
        score_tickers = sorted({score.ticker for score in score_data})
        score_columns = {
            "AI Use Score": "ai_use_score",
            "Readiness Score": "readiness_score",
            "Talk Ratio (%)": "talk_ratio_pct",
        }
        summary_columns = st.columns(3)
        summary_columns[0].metric("Firm-year scores", len(score_data))
        summary_columns[1].metric("Firms with scores", len(score_tickers))
        summary_columns[2].metric(
            "Fiscal-year coverage",
            f"{score_years[0]}–{score_years[-1]}",
        )

        preferred_year = 2025 if 2025 in score_years else score_years[-1]
        selected_year = st.selectbox(
            "Fiscal year for firm comparison",
            score_years,
            index=score_years.index(preferred_year),
        )
        ticker_labels = {firm["ticker"]: firm["company"] for firm in FIRMS}
        selected_score_tickers = st.multiselect(
            "Firms to include",
            score_tickers,
            default=score_tickers,
            format_func=lambda ticker: ticker_labels[ticker],
        )

        score_lookup = {
            (score.ticker, score.fiscal_year): score for score in score_data
        }
        table_rows = []
        for firm in FIRMS:
            ticker = firm["ticker"]
            if ticker not in selected_score_tickers:
                continue
            score = score_lookup.get((ticker, selected_year))
            if score is None:
                table_rows.append({
                    "Company": firm["company"],
                    "Ticker": ticker,
                    "Fiscal year": selected_year,
                    "Status": "No score available",
                    "AI Use Score": None,
                    "Scenarios with use": None,
                    "Readiness Score": None,
                    "Talk Ratio (%)": None,
                    "Substantive passages": None,
                })
            else:
                table_rows.append({
                    "Company": score.company,
                    "Ticker": score.ticker,
                    "Fiscal year": score.fiscal_year,
                    "Status": "Scored",
                    "AI Use Score": score.ai_use_score,
                    "Scenarios with use": ", ".join(score.scenarios_with_use) or "None scored",
                    "Readiness Score": score.readiness_score,
                    "Talk Ratio (%)": score.talk_ratio_pct,
                    "Substantive passages": score.substantive_ai_passages,
                })
        st.dataframe(pd.DataFrame(table_rows), hide_index=True, width="stretch")

        if selected_score_tickers:
            selected_metric = st.selectbox("Annual trend metric", list(score_columns))
            metric_column = score_columns[selected_metric]
            trend_chart = go.Figure()
            for ticker in selected_score_tickers:
                by_year = {
                    score.fiscal_year: score
                    for score in score_data
                    if score.ticker == ticker
                }
                trend_chart.add_trace(
                    go.Scatter(
                        name=ticker_labels[ticker],
                        x=score_years,
                        y=[
                            getattr(by_year[year], metric_column)
                            if year in by_year
                            else None
                            for year in score_years
                        ],
                        mode="lines+markers",
                        connectgaps=False,
                        hovertemplate="%{x}: %{y}<extra>%{fullData.name}</extra>",
                    )
                )
            trend_chart.update_layout(
                **chart_layout(f"Annual {selected_metric.lower()} · SEC pilot", selected_metric),
            )
            trend_chart.update_xaxes(dtick=1)
            trend_chart.update_yaxes(rangemode="tozero")
            st.plotly_chart(
                trend_chart,
                width="stretch",
                config={"displayModeBar": False},
            )
        else:
            st.info("Select at least one firm to view annual score trends.")

with story_tab:
    records = sorted(
        get_use_cases(selected_ticker),
        key=lambda record: (
            int(record["quarter"][:4]),
            int(record["quarter"][-1]),
        ),
        reverse=True,
    )
    summary = summarize_use_cases(selected_ticker)
    firm_label = selected_firm["company"]

    st.subheader(firm_label)
    st.caption(f"{selected_firm['sector']} · {selected_firm['ticker']} · fictional demo records")

    st.markdown("### Envisioned demo overview")
    st.write(
        f"This walkthrough contains **{summary['record_count']} invented example records** "
        f"across **{summary['area_count']} example areas**. "
        f"They demonstrate how a future evidence-backed firm view might be organized; "
        f"they do not describe {firm_label}."
    )
    metric_columns = st.columns(3)
    metric_columns[0].metric("Fictional records", summary["record_count"], "Demo only")
    metric_columns[1].metric("Example areas", summary["area_count"], "Demo labels, not taxonomy")
    latest = summary["latest_record"]
    metric_columns[2].metric(
        "Latest example period", latest["quarter"] if latest else "—", "Invented timeline"
    )

    stage_columns = st.columns(len(DEMO_STAGES))
    for column, stage in zip(stage_columns, DEMO_STAGES):
        column.metric(
            f"Demo stage · {stage}",
            summary["stage_counts"].get(stage, 0),
            "Count of fictional records",
        )

    st.markdown("### Browse envisioned use cases")
    st.caption(
        "Open any card to explore its fictional summary and details. The area and stage labels "
        "are interface examples, not the project's approved categories or scoring rules."
    )
    st.markdown("### Fictional example timeline")
    st.caption(
        "Cumulative count of invented demo records by their made-up period. This is a UI "
        "timeline—not a measure of real company activity or adoption."
    )
    timeline = compare_timeline([selected_ticker])
    firm_timeline = [row for row in timeline if row["ticker"] == selected_ticker]
    timeline_chart = go.Figure(
        go.Scatter(
            name="Cumulative fictional records",
            x=[row["quarter"] for row in firm_timeline],
            y=[row["cumulative_examples"] for row in firm_timeline],
            mode="lines+markers",
            line={"color": COLORS["accent"], "width": 3, "shape": "hv"},
            marker={"color": COLORS["structural"], "size": 8},
            hovertemplate="%{x}<br>%{y} fictional records<extra></extra>",
        )
    )
    timeline_chart.update_layout(
        **chart_layout("Cumulative fictional demo records", "Cumulative demo records"),
        showlegend=False,
    )
    timeline_chart.update_yaxes(dtick=1, rangemode="tozero")
    st.plotly_chart(timeline_chart, width="stretch", config={"displayModeBar": False})

    st.markdown("#### Open a fictional use case")
    with st.container(key="use_case_stack"):
        for index, record in enumerate(records):
            expanded_key = f"expanded_use_case_{record['id']}"
            if expanded_key not in st.session_state:
                st.session_state[expanded_key] = index == 0

            stage_class = {
                "Exploring": "exploring",
                "Pilot": "pilot",
                "In use": "in_use",
            }[record["stage"]]
            quarter = record["quarter"].split()
            quarter_label = f"Q{quarter[1][1:]} {quarter[0]}"
            card_state = "open" if st.session_state[expanded_key] else "closed"

            with st.container(key=f"use_case_card_{card_state}_{record['id']}"):
                title_column, stage_column, quarter_column, toggle_column = st.columns(
                    [5, 1.55, 1.25, 0.6],
                    vertical_alignment="center",
                )
                title_column.markdown(
                    f'<div class="use-case-title">{escape(record["title"])}</div>',
                    unsafe_allow_html=True,
                )
                stage_column.markdown(
                    f'<div class="use-case-badge stage-{stage_class}">'
                    f"{escape(record['stage'])}</div>",
                    unsafe_allow_html=True,
                )
                quarter_column.markdown(
                    f'<div class="use-case-badge quarter-badge">'
                    f"{escape(quarter_label)}</div>",
                    unsafe_allow_html=True,
                )
                action = "Close" if st.session_state[expanded_key] else "Open"
                toggle_label = f"{action} {record['title']} details"
                if toggle_column.button(
                    toggle_label,
                    key=f"toggle_{expanded_key}",
                    width="stretch",
                    type="tertiary",
                ):
                    st.session_state[expanded_key] = not st.session_state[expanded_key]
                    st.rerun()

                if st.session_state[expanded_key]:
                    st.markdown(
                        f'<div class="use-case-summary"><strong>'
                        f"{escape(record['area'])}:</strong> "
                        f"{escape(record['summary'])}</div>",
                        unsafe_allow_html=True,
                    )
                    st.caption(record["detail"])
                    st.markdown(
                        '<div class="use-case-evidence"><strong>Evidence preview:</strong> '
                        "No real source is attached. A future research view would show a "
                        "reviewed citation here; this demo does not fabricate one.</div>",
                        unsafe_allow_html=True,
                    )

    st.markdown("### What this story is showing")
    st.write(
        f"The overview and timeline summarize these same {len(records)} fictional records. "
        "Each card opens to show its mock details and an empty evidence preview. All counts "
        "come from demo fixtures, not company research."
    )

with compare_tab:
    st.markdown("### Compare envisioned firms")
    st.write(
        "Select two or more firms to compare the areas, example records, and demo stages in their "
        "fictional walkthroughs. Real companies are not being compared on actual AI adoption."
    )

    compare_sector_options = ["All sectors", *sectors]
    compare_sector = st.selectbox(
        "Limit selector by sector", compare_sector_options, index=0, key="compare_sector"
    )
    compare_firms = get_firms(None if compare_sector == "All sectors" else compare_sector)
    compare_options = {firm["ticker"]: firm["company"] for firm in compare_firms}
    default_compare = [
        ticker for ticker in (selected_ticker, "BAC", "COF")
        if ticker in compare_options
    ][:3]
    selected_tickers = st.multiselect(
        "Firms to compare",
        list(compare_options),
        default=default_compare,
        format_func=lambda ticker: compare_options[ticker],
    )
    if len(selected_tickers) < 2:
        st.info("Choose at least two firms to see a side-by-side comparison.")
    else:
        comparison = compare_use_cases(selected_tickers)
        st.caption(
            "Every row and bar is derived from fictional records above. Compare this demo "
            "interface, not real firms."
        )
        st.dataframe(pd.DataFrame(comparison), hide_index=True, width="stretch")

        timeline_rows = compare_timeline(selected_tickers)
        timeline_chart = go.Figure()
        for index, ticker in enumerate(selected_tickers):
            firm_rows = [row for row in timeline_rows if row["ticker"] == ticker]
            timeline_chart.add_trace(
                go.Scatter(
                    name=f"{firm_rows[0]['company']} · fictional records",
                    x=[row["quarter"] for row in firm_rows],
                    y=[row["cumulative_examples"] for row in firm_rows],
                    mode="lines+markers",
                    line={
                        "color": CHART_PALETTE[index % len(CHART_PALETTE)],
                        "width": 2.5,
                        "shape": "hv",
                    },
                    marker={"size": 7},
                    hovertemplate="%{x}<br>%{y} fictional records<extra></extra>",
                )
            )
        timeline_chart.update_layout(
            **chart_layout(
                "Cumulative fictional records by demo quarter",
                "Cumulative demo records",
            ),
        )
        timeline_chart.update_yaxes(dtick=1, rangemode="tozero")
        st.caption(
            "Each line is a cumulative count of invented records attached to a selector firm. "
            "It shows how demo examples are distributed over the fictional timeline—not adoption."
        )
        st.plotly_chart(timeline_chart, width="stretch", config={"displayModeBar": False})

        stage_chart = go.Figure()
        for stage in DEMO_STAGES:
            stage_chart.add_trace(
                go.Bar(
                    name=f"Demo stage · {stage}",
                    x=[row["company"] for row in comparison],
                    y=[row["stage_counts"].get(stage, 0) for row in comparison],
                    marker_color=STAGE_COLORS[stage],
                )
            )
        stage_chart.update_layout(
            **chart_layout("Fictional records by demo stage", "Number of demo records"),
            barmode="group",
        )
        stage_chart.update_yaxes(dtick=1, rangemode="tozero")
        st.plotly_chart(stage_chart, width="stretch", config={"displayModeBar": False})

        area_chart = go.Figure()
        for index, area in enumerate(DEMO_AREAS):
            area_chart.add_trace(
                go.Bar(
                    name=f"Example area · {area}",
                    x=[row["company"] for row in comparison],
                    y=[row["area_counts"].get(area, 0) for row in comparison],
                    marker_color=CHART_PALETTE[index % len(CHART_PALETTE)],
                )
            )
        area_chart.update_layout(
            **chart_layout("Fictional records by example area", "Number of demo records"),
            barmode="stack",
        )
        area_chart.update_yaxes(dtick=1, rangemode="tozero")
        st.plotly_chart(area_chart, width="stretch", config={"displayModeBar": False})

with about_tab:
    st.markdown("### What is real and scored")
    st.markdown(
        "- `data/processed/sec/company_scores_v0.csv` contains annual scores derived from SEC filing passages.\n"
        "- AI Use Score, Readiness Score, Talk Ratio, scenario codes, and substantive-passage counts "
        "are computed values from the current v0 scoring pipeline.\n"
        "- The underlying v0 passage labels were AI-assisted drafts. Treat these as preliminary "
        "disclosure-based scores, not verified firm-wide AI adoption or a final index.\n"
        "- FY2026 is partial through June 30, 2026; Citi and Principal have no FY2023 score. "
        "Unavailable years are not interpreted as zero.\n"
        "- The score CSV does not include evidence IDs or citations, so the real-data view cannot "
        "drill down to supporting passages."
    )
    st.markdown("### What is envisioned / fictional")
    st.markdown(
        "- The firm-story and comparison tabs use invented use-case titles, summaries, details, "
        "areas, stages, quarterly dates, counts, and chart values from `src/dashboard/mock_data.py`.\n"
        "- These examples illustrate a possible future evidence-backed experience. They are not "
        "research findings, company claims, or scores, and they are never joined to the SEC score table.\n"
        "- The envisioned cards have no attached real sources or fabricated citations."
    )
    st.markdown("### Fictional example records used by the mockup")
    st.dataframe(
        records_frame(get_use_cases()),
        hide_index=True,
        width="stretch",
    )

st.caption(
    "Preliminary SEC disclosure scores · Separate fictional interface examples · "
    "Not for investment use"
)
