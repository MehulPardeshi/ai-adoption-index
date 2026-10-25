"""Interactive Streamlit journey built only from explicitly fictional demo records."""

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
from src.dashboard.theme import (
    BODY_FONT,
    CHART_PALETTE,
    COLORS,
    HEADING_FONT,
    STAGE_COLORS,
    THEME_CSS,
)

st.set_page_config(
    page_title="AI Activity | Financial Services",
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


st.markdown('<div class="eyebrow">Financial services · interactive demo</div>', unsafe_allow_html=True)
st.title("AI Use Case Index (Demo)")
st.write(
    "Follow one firm’s fictional example records, open a use case, then compare the same "
    "kind of demo records across firms."
)
st.warning(
    "**DEMO ONLY — NOT COMPANY CLAIMS.** Real firm names are used only to make the selector "
    "familiar. Every use case, date, description, stage, summary, and comparison below is "
    "invented for this interface. No real company data, sources, research rules, scoring, "
    "model, or API are connected."
)

sectors = sorted({firm["sector"] for firm in FIRMS})
with st.sidebar:
    st.markdown("### 1 · Choose a firm")
    selected_sector = st.selectbox("Sector", ["All sectors", *sectors], index=0)
    sector_filter = None if selected_sector == "All sectors" else selected_sector
    sector_firms = get_firms(sector_filter)
    firm_labels = {firm["ticker"]: firm["company"] for firm in sector_firms}
    selected_ticker = st.selectbox(
        "Company", list(firm_labels), format_func=lambda ticker: firm_labels[ticker]
    )
    selected_firm = next(firm for firm in sector_firms if firm["ticker"] == selected_ticker)
    st.caption("Filters change the fictional records only.")

story_tab, compare_tab, about_tab = st.tabs(
    ["Firm story", "Compare firms", "About this demo"]
)

with story_tab:
    records = get_use_cases(selected_ticker)
    summary = summarize_use_cases(selected_ticker)
    firm_label = selected_firm["company"]

    st.subheader(firm_label)
    st.caption(f"{selected_firm['sector']} · {selected_firm['ticker']} · fictional demo records")

    st.markdown("### 2 · Get the overview")
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

    st.markdown("### 3 · Browse the example use cases")
    st.caption(
        "The area and stage labels below exist only to demonstrate navigation and filtering. "
        "They are not the project's approved categories or scoring rules."
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
    st.dataframe(records_frame(records), hide_index=True, width="stretch")

    st.markdown("### 4 · Open a record")
    record_ids = {record["id"]: record for record in records}
    selected_record_id = st.selectbox(
        "Select a fictional use case",
        list(record_ids),
        format_func=lambda record_id: (
            f"{record_ids[record_id]['quarter']} · {record_ids[record_id]['title']}"
        ),
    )
    selected_record = record_ids[selected_record_id]
    st.markdown(f"#### {selected_record['title']}")
    detail_columns = st.columns([1, 2])
    detail_columns[0].write(f"**Period:** {selected_record['quarter']}")
    detail_columns[0].write(f"**Example area:** {selected_record['area']}")
    detail_columns[0].write(f"**Demo stage:** {selected_record['stage']}")
    detail_columns[1].write(selected_record["summary"])
    detail_columns[1].caption(selected_record["detail"])
    st.info(
        "**Evidence preview:** no real source is attached. A future research view would show "
        "a reviewed citation here; this demo does not fabricate one."
    )

    st.markdown("### What this story is showing")
    st.write(
        f"The overview counts these same {len(records)} fictional records; the table lists them; selecting "
        "one opens its details. The totals and stage counts are calculated from the demo records, "
        "not from company research."
    )

with compare_tab:
    st.markdown("### 5 · Compare firms")
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
    st.markdown("### This is an interface walkthrough, not a result")
    st.markdown(
        "- The firm names and sectors are selector labels from the planned demo cohort.\n"
        "- Every use-case title, date, area, stage, detail, count, and chart value is invented.\n"
        "- The use-case areas and stages are interface examples—not the project's finalized "
        "taxonomy, metrics, or scoring rules.\n"
        "- This app reads only `src/dashboard/mock_data.py`; it does not load research datasets, "
        "filings, source passages, labels, or citations.\n"
        "- It does not call an agent, model, or API and does not write research outputs."
    )
    st.markdown("### Use-case records currently in the demo")
    st.dataframe(
        records_frame(get_use_cases()),
        hide_index=True,
        width="stretch",
    )

st.caption(
    "Explicitly fictional interface demo · Real firm names are not evidence · "
    "Not for research or investment use"
)
