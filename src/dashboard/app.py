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
from src.dashboard.score_data import (
    SCORE_METRIC_HELP,
    complete_fiscal_year_scores,
    format_scenario_code,
    load_company_scores,
    validate_firm_labels,
)
from src.dashboard.theme import (
    BODY_FONT,
    CHART_PALETTE,
    COLORS,
    HEADING_FONT,
    STAGE_COLORS,
    THEME_CSS,
    book_title,
)

st.set_page_config(
    page_title="AI Adoption Index | SEC Pilot",
    layout="wide",
    initial_sidebar_state="collapsed",
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
            "Illustrative use case": book_title(record["title"]),
            "Example area": record["area"],
            "Demo stage": record["stage"],
        }
        for record in records
    ])


def render_score_metric_help(metric_names):
    """Render visible, click-to-open definitions beside the score metric labels."""
    st.caption("Select the ? beside a metric to learn how it is calculated.")
    help_columns = st.columns(len(metric_names))
    metric_keys = {
        "AI Use Score": "ai_use_score",
        "Readiness Score": "readiness_score",
        "Talk Ratio (%)": "talk_ratio",
    }
    active_metric = st.session_state.get("active_score_metric_help")
    for column, metric in zip(help_columns, metric_names):
        label_column, button_column = column.columns(
            [0.85, 0.15],
            vertical_alignment="center",
        )
        label_column.markdown(f"**{metric}**")
        with button_column:
            if st.button(
                "?",
                key=f"score_help_{metric_keys[metric]}",
                help=f"Click to learn about {metric}",
            ):
                st.session_state["active_score_metric_help"] = (
                    None if active_metric == metric else metric
                )
                active_metric = st.session_state["active_score_metric_help"]

    if active_metric:
        st.info(f"**{active_metric}.** {SCORE_METRIC_HELP[active_metric]}")


st.markdown('<div class="eyebrow">Financial Services · Research Preview</div>', unsafe_allow_html=True)
st.title("AI Adoption Index | SEC Pilot + Envisioned Demo")
st.write(
    "Explore preliminary annual scores calculated from SEC filing labels, then switch to a "
    "separate fictional walkthrough of an envisioned evidence-backed dashboard."
)
with st.container(key="global_disclaimer"):
    st.warning(
        "**Two Distinct Data Tracks.** The SEC pilot tab shows preliminary scores calculated from "
        "SEC disclosure passages and AI-assisted v0 labels; these are not verified measures of "
        "firm-wide adoption. The envisioned tabs use fictional records, dates, categories, and "
        "stages for interface demonstration only. Never interpret those mock examples as company claims."
    )

score_data = None
score_data_error = None
try:
    score_data = load_company_scores()
    validate_firm_labels(score_data, FIRMS)
    score_data = complete_fiscal_year_scores(score_data)
    if not score_data:
        score_data_error = "No complete fiscal-year scores are available to display."
except (OSError, ValueError, csv.Error) as exc:
    score_data_error = str(exc)

scores_tab, story_tab, compare_tab, about_tab = st.tabs(
    ["SEC Pilot Scores", "Envisioned Firm Story", "Envisioned Comparison", "About the Data"]
)

with scores_tab:
    st.subheader("Preliminary SEC Disclosure Scores")
    st.write(
        "Each row is a company–fiscal-year score calculated from labeled SEC filing passages. "
        "These are disclosure-based pilot metrics, not a census of a firm's AI activity or a "
        "final adoption index."
    )
    with st.container(key="score_disclaimer"):
        st.warning(
            "**Preliminary / AI-Assisted V0.** The current score file uses AI-assisted draft "
            "passage labels and the v0 scoring method. A score of 0 means no scored use was found "
            "in the available labeled disclosures; it does not establish that the firm does not use AI."
        )
    st.caption(
        "The source contains annual observations. FY2026 is partial through June 30, 2026, so "
        "it is excluded from this comparison and trend; its source rows are retained. Citi and "
        "Principal have no FY2023 score. Missing firm-years are unavailable, never zero. The "
        "source has no evidence IDs or citations, so this view has no passage-level drill-down."
    )

    if score_data_error:
        st.error(f"Could not display the SEC score view: {score_data_error}")
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
            "Fiscal-year coverage (complete years)",
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
                    "Scenarios with use": (
                        ", ".join(
                            format_scenario_code(code)
                            for code in score.scenarios_with_use
                        )
                        or "None scored"
                    ),
                    "Readiness Score": score.readiness_score,
                    "Talk Ratio (%)": score.talk_ratio_pct,
                    "Substantive passages": score.substantive_ai_passages,
                })
        render_score_metric_help(score_columns)
        st.dataframe(
            pd.DataFrame(table_rows),
            column_config={
                "AI Use Score": st.column_config.NumberColumn(
                    "AI Use Score",
                    help=SCORE_METRIC_HELP["AI Use Score"],
                    format="%d",
                ),
                "Readiness Score": st.column_config.NumberColumn(
                    "Readiness Score",
                    help=SCORE_METRIC_HELP["Readiness Score"],
                    format="%d",
                ),
                "Talk Ratio (%)": st.column_config.NumberColumn(
                    "Talk Ratio (%)",
                    help=SCORE_METRIC_HELP["Talk Ratio (%)"],
                    format="%d%%",
                ),
                "Scenarios with use": st.column_config.TextColumn(
                    "Scenarios with use",
                    help=(
                        "Scenario codes and names follow the frozen taxonomy codebook. "
                        "These are categories in the current preliminary score file, not "
                        "passage-level evidence or a list of verified deployments."
                    ),
                ),
            },
            hide_index=True,
            width="stretch",
        )

        if selected_score_tickers:
            selected_metric = st.selectbox(
                "Annual trend metric",
                list(score_columns),
                help=(
                    "Definitions are available by hovering over the corresponding metric "
                    "column header in the score table."
                ),
            )
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
                **chart_layout(f"Annual {selected_metric} · SEC Pilot", selected_metric),
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
    sectors = sorted({firm["sector"] for firm in FIRMS})
    filter_columns = st.columns(2)
    selected_sector = filter_columns[0].selectbox(
        "Sector",
        ["All sectors", *sectors],
        index=0,
        key="story_sector",
    )
    sector_filter = None if selected_sector == "All sectors" else selected_sector
    sector_firms = get_firms(sector_filter)
    firm_labels = {firm["ticker"]: firm["company"] for firm in sector_firms}
    selected_ticker = filter_columns[1].selectbox(
        "Company",
        list(firm_labels),
        format_func=lambda ticker: firm_labels[ticker],
        key="story_company",
    )
    selected_firm = next(firm for firm in sector_firms if firm["ticker"] == selected_ticker)
    st.caption("These selectors filter the fictional firm-story walkthrough only.")

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

    st.markdown("### Envisioned Demo Overview")
    st.write(
        f"This walkthrough contains **{summary['record_count']} invented example records** "
        f"across **{summary['area_count']} example areas**. "
        f"They demonstrate how a future evidence-backed firm view might be organized; "
        f"they do not describe {firm_label}."
    )
    latest = summary["latest_record"]
    overview_columns = st.columns(3)
    overview_columns[0].metric(
        "Fictional records",
        summary["record_count"],
        "Demo only",
    )
    overview_columns[1].metric(
        "Example areas",
        f"{summary['area_count']} of {len(DEMO_AREAS)}",
        "Fictional demo labels",
    )
    with overview_columns[2]:
        st.markdown("**Stage mix**")
        stage_mix_chart = go.Figure()
        for stage in DEMO_STAGES:
            stage_mix_chart.add_trace(
                go.Bar(
                    name=stage,
                    x=[summary["stage_counts"].get(stage, 0)],
                    y=[""],
                    orientation="h",
                    marker={"color": STAGE_COLORS[stage]},
                    hovertemplate=(
                        f"{stage}: %{{x}} fictional demo records<extra></extra>"
                    ),
                )
            )
        stage_mix_chart.update_layout(
            barmode="stack",
            height=122,
            margin={"l": 0, "r": 0, "t": 4, "b": 30},
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            font={"family": BODY_FONT, "color": COLORS["text"]},
            legend={"orientation": "h", "x": 0, "y": -0.2, "font": {"size": 11}},
        )
        stage_mix_chart.update_xaxes(visible=False, showgrid=False, zeroline=False)
        stage_mix_chart.update_yaxes(visible=False, showgrid=False, zeroline=False)
        st.plotly_chart(
            stage_mix_chart,
            width="stretch",
            config={"displayModeBar": False},
        )

    with st.expander("More Demo Details"):
        latest_period = latest["quarter"] if latest else "No example records"
        st.write(f"Latest fictional example period: **{latest_period}**")
        stage_details = " · ".join(
            f"{stage}: {summary['stage_counts'].get(stage, 0)}"
            for stage in DEMO_STAGES
        )
        st.write(f"Fictional stage counts: {stage_details}")

    st.markdown("### Browse Envisioned Use Cases")
    st.caption(
        "Open any card to explore its fictional summary and details. The area and stage labels "
        "are interface examples, not the project's approved categories or scoring rules."
    )
    st.markdown("### Fictional Example Timeline")
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
        **chart_layout("Cumulative Fictional Demo Records", "Cumulative demo records"),
        showlegend=False,
    )
    timeline_chart.update_yaxes(dtick=1, rangemode="tozero")
    st.plotly_chart(timeline_chart, width="stretch", config={"displayModeBar": False})

    st.markdown("#### Open a Fictional Use Case")
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
                    f'<div class="use-case-title">'
                    f"{escape(book_title(record['title']))}</div>",
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
                toggle_label = f"{action} {book_title(record['title'])} Details"
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

    st.markdown("### What This Story Is Showing")
    st.write(
        f"The overview and timeline summarize these same {len(records)} fictional records. "
        "Each card opens to show its mock details and an empty evidence preview. All counts "
        "come from demo fixtures, not company research."
    )

with compare_tab:
    st.markdown("### Compare Envisioned Firms")
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
                "Cumulative Fictional Records by Demo Quarter",
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
            **chart_layout("Fictional Records by Demo Stage", "Number of demo records"),
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
            **chart_layout("Fictional Records by Example Area", "Number of demo records"),
            barmode="stack",
        )
        area_chart.update_yaxes(dtick=1, rangemode="tozero")
        st.plotly_chart(area_chart, width="stretch", config={"displayModeBar": False})

with about_tab:
    st.markdown("### What Is Real and Scored")
    st.markdown(
        "- `data/processed/sec/company_scores_v0.csv` contains annual scores derived from SEC 10-K and 10-Q filing passages.\n"
        "- AI Use Score, Readiness Score, Talk Ratio, scenario codes, and substantive-passage counts "
        "are computed values from the current v0 scoring pipeline.\n"
        "- The underlying v0 passage labels were AI-assisted drafts. Treat these as preliminary "
        "disclosure-based scores, not verified firm-wide AI adoption or a final index.\n"
        "- The dashboard score table and trends hide FY2026 because source filings are only "
        "available through June 30, 2026; those partial-year rows remain in the source file. "
        "Citi and Principal have no FY2023 score. Unavailable years are not interpreted as zero.\n"
        "- Scenario codes are displayed with names from the frozen taxonomy codebook. The "
        "dashboard still reads the existing AI-assisted v0 score file; it does not yet integrate "
        "the latest agreed human labels or recalculate scores from them.\n"
        "- The client has not yet confirmed whether the dashboard should use 10-K only or 10-K "
        "plus 10-Q, or whether to display more specific use cases beside scores. The current "
        "source remains 10-K plus 10-Q pending that discussion.\n"
        "- The score CSV does not include evidence IDs or citations, so the real-data view cannot "
        "drill down to supporting passages."
    )
    st.markdown("### What Is Envisioned / Fictional")
    st.markdown(
        "- The firm-story and comparison tabs use invented use-case titles, summaries, details, "
        "areas, stages, quarterly dates, counts, and chart values from `src/dashboard/mock_data.py`.\n"
        "- These examples illustrate a possible future evidence-backed experience. They are not "
        "research findings, company claims, or scores, and they are never joined to the SEC score table.\n"
        "- The envisioned cards have no attached real sources or fabricated citations."
    )
    st.markdown("### Fictional Example Records Used by the Mockup")
    st.dataframe(
        records_frame(get_use_cases()),
        hide_index=True,
        width="stretch",
    )

st.caption(
    "Preliminary SEC disclosure scores · Separate fictional interface examples · "
    "Not for investment use"
)
