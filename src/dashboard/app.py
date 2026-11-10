"""Streamlit dashboard for consensus-based company scores and sector indexes."""

import csv

import pandas as pd
import plotly.graph_objects as go
import streamlit as st

from src.dashboard.score_data import (
    FIRM_LABELS,
    SCORE_METRIC_HELP,
    SectorYearIndex,
    complete_fiscal_year_scores,
    complete_sector_index_years,
    format_scenario_code,
    load_company_scores,
    load_sector_index,
    validate_firm_labels,
)
from src.dashboard.theme import (
    BODY_FONT,
    CHART_PALETTE,
    COLORS,
    HEADING_FONT,
    THEME_CSS,
    book_title,
)


st.set_page_config(
    page_title="AI Adoption Index | Financial Firms",
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
        "yaxis": {
            "title": y_title,
            "gridcolor": COLORS["border"],
            "zerolinecolor": COLORS["border"],
        },
        "legend": {"orientation": "h", "y": -0.22},
        "hovermode": "closest",
    }


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


SECTOR_COLUMN_HELP = {
    "Fiscal year": (
        "The fiscal year for the annual SEC filings used in the index. FY2026 is hidden "
        "because it is incomplete."
    ),
    "Firms in index": (
        "Count of core proof-of-concept firms included that year. The six-company sample "
        "is JPMorgan Chase, Bank of America, Capital One, Wells Fargo, Charles Schwab, "
        "and Principal Financial Group. Citigroup is a benchmark and is excluded."
    ),
    "Equal-weighted score": (
        "The arithmetic average of the included firms' AI Use Scores. Each firm has the "
        "same weight, regardless of size."
    ),
    "Market-cap-weighted score": (
        "The included firms' AI Use Scores weighted by public float from SEC filings. "
        "Larger public-float values contribute more to the index."
    ),
    "Public float (USD)": (
        "The sum of the included firms' public float for that year: the market value of "
        "shares held by non-affiliates, as reported in SEC filings."
    ),
}

SECTOR_COLUMN_KEYS = {
    "Fiscal year": "fiscal_year",
    "Firms in index": "firms_in_index",
    "Equal-weighted score": "equal_weighted_score",
    "Market-cap-weighted score": "market_cap_weighted_score",
    "Public float (USD)": "public_float_usd",
}


def render_sector_table_help():
    """Render visible, click-to-open definitions for the sector table columns."""
    st.caption("Select the ? beside a column to learn what it means.")
    active_column = st.session_state.get("active_sector_column_help")
    with st.container(key="sector_help_row"):
        help_columns = st.columns(len(SECTOR_COLUMN_HELP))
        for column, label in zip(help_columns, SECTOR_COLUMN_HELP):
            with column:
                st.markdown(
                    '<div class="sector-help-heading">'
                    f"<strong>{label}</strong>"
                    "</div>",
                    unsafe_allow_html=True,
                )
                with st.container(key=f"sector_help_button_{SECTOR_COLUMN_KEYS[label]}"):
                    if st.button(
                        "?",
                        key=f"sector_help_{SECTOR_COLUMN_KEYS[label]}",
                        help=f"Click to learn about {label}",
                    ):
                        st.session_state["active_sector_column_help"] = (
                            None if active_column == label else label
                        )
                        active_column = st.session_state["active_sector_column_help"]

    if active_column:
        st.info(f"**{active_column}.** {SECTOR_COLUMN_HELP[active_column]}")


def sector_index_frame(rows: tuple[SectorYearIndex, ...]) -> pd.DataFrame:
    return pd.DataFrame(
        [
            {
                "Fiscal year": row.fiscal_year,
                "Firms in index": row.n_firms,
                "Equal-weighted score": row.ai_ew,
                "Market-cap-weighted score": row.ai_cw,
                "Public float (USD)": row.total_public_float_usd,
            }
            for row in rows
        ]
    )


st.markdown(
    '<div class="eyebrow">Financial Services · Research Preview</div>',
    unsafe_allow_html=True,
)
st.title(book_title("AI Adoption Index | Financial Firms"))
st.write(
    "Explore annual SEC disclosure scores for individual firms and the six-firm "
    "equal-weighted and market-cap-weighted index."
)
with st.container(key="global_disclaimer"):
    st.warning(
        "**Label coverage:** 80 of 277 passages have human-agreed labels; the remainder "
        "use AI-draft labels. Scores summarize SEC disclosures and are not verified "
        "measures of firm-wide AI adoption."
    )

score_data_error = None
sector_index_error = None
score_data = None
sector_index = None
try:
    score_data = load_company_scores()
    validate_firm_labels(score_data)
    score_data = complete_fiscal_year_scores(score_data)
    if not score_data:
        score_data_error = "No complete fiscal-year company scores are available."
except (OSError, ValueError, csv.Error) as exc:
    score_data_error = str(exc)

try:
    sector_index = complete_sector_index_years(load_sector_index())
    if not sector_index:
        sector_index_error = "No complete fiscal-year sector index rows are available."
except (OSError, ValueError, csv.Error) as exc:
    sector_index_error = str(exc)

sector_tab, company_tab, about_tab = st.tabs(
    ["Sector Overview", "Company Scores", "About the Data"]
)

with sector_tab:
    st.subheader("Six-Firm Financial-Company Index")
    st.write(
        "Here, “financial sector” means our selected six-company proof-of-concept sample, "
        "not every financial-services firm or a standard market-sector index. The sample "
        "includes banks, a wealth firm, and a retirement-services firm. Compare annual AI "
        "Use Scores across the six core proof-of-concept firms. "
        "The equal-weighted and market-cap-weighted series use the same firm-year scores; "
        "Citigroup remains an individual-firm benchmark and is excluded here."
    )
    if sector_index_error:
        st.error(f"Could not display the sector index: {sector_index_error}")
    elif sector_index:
        latest_index = sector_index[-1]
        summary_columns = st.columns(3)
        summary_columns[0].metric("Latest complete fiscal year", latest_index.fiscal_year)
        summary_columns[1].metric("Firms in index", latest_index.n_firms)
        summary_columns[2].metric(
            "AI Use Score (equal / cap weighted)",
            f"{latest_index.ai_ew:.1f} / {latest_index.ai_cw:.1f}",
        )

        years = [row.fiscal_year for row in sector_index]
        index_chart = go.Figure()
        for name, attribute, color in (
            ("Equal-weighted (AI-EW)", "ai_ew", CHART_PALETTE[0]),
            ("Market-cap-weighted (AI-CW)", "ai_cw", CHART_PALETTE[1]),
        ):
            index_chart.add_trace(
                go.Scatter(
                    name=name,
                    x=years,
                    y=[getattr(row, attribute) for row in sector_index],
                    mode="lines+markers",
                    line={"color": color, "width": 3},
                    marker={"size": 8},
                    hovertemplate="%{x}: %{y:.1f}<extra>%{fullData.name}</extra>",
                )
            )
        index_chart.update_layout(
            **chart_layout("Annual Sector AI Use Score", "AI Use Score (0–100)")
        )
        index_chart.update_xaxes(dtick=1)
        index_chart.update_yaxes(rangemode="tozero")
        st.plotly_chart(
            index_chart,
            width="stretch",
            config={"displayModeBar": False},
        )
        st.caption(
            "The sector series covers six core firms with a 10-K and public-float value "
            "for that year. FY2026 is not included because it is incomplete."
        )
        render_sector_table_help()
        st.dataframe(
            sector_index_frame(sector_index),
            column_config={
                "Fiscal year": st.column_config.NumberColumn(
                    help=SECTOR_COLUMN_HELP["Fiscal year"],
                    format="%d",
                ),
                "Firms in index": st.column_config.NumberColumn(
                    help=SECTOR_COLUMN_HELP["Firms in index"],
                    format="%d",
                ),
                "Equal-weighted score": st.column_config.NumberColumn(
                    help=SECTOR_COLUMN_HELP["Equal-weighted score"],
                    format="%.1f",
                ),
                "Market-cap-weighted score": st.column_config.NumberColumn(
                    help=SECTOR_COLUMN_HELP["Market-cap-weighted score"],
                    format="%.1f",
                ),
                "Public float (USD)": st.column_config.NumberColumn(
                    help=SECTOR_COLUMN_HELP["Public float (USD)"],
                    format="$%d",
                ),
            },
            hide_index=True,
            width="stretch",
        )

with company_tab:
    st.subheader("Individual Firm Scores")
    st.write(
        "Review annual scores and reported use-case categories by company. Missing "
        "company-years are shown as unavailable, not as zero."
    )
    if score_data_error:
        st.error(f"Could not display company scores: {score_data_error}")
    elif score_data:
        score_years = sorted({score.fiscal_year for score in score_data})
        score_tickers = [
            ticker for ticker in FIRM_LABELS
            if any(score.ticker == ticker for score in score_data)
        ]
        score_columns = {
            "AI Use Score": "ai_use_score",
            "Readiness Score": "readiness_score",
            "Talk Ratio (%)": "talk_ratio_pct",
        }

        selector_columns = st.columns([1, 2])
        selected_year = selector_columns[0].selectbox(
            "Fiscal year for firm comparison",
            score_years,
            index=score_years.index(2025) if 2025 in score_years else len(score_years) - 1,
        )
        selected_score_tickers = selector_columns[1].multiselect(
            "Firms to include",
            score_tickers,
            default=score_tickers,
            format_func=lambda ticker: FIRM_LABELS[ticker],
        )

        score_lookup = {
            (score.ticker, score.fiscal_year): score for score in score_data
        }
        table_rows = []
        for ticker in selected_score_tickers:
            score = score_lookup.get((ticker, selected_year))
            if score is None:
                table_rows.append(
                    {
                        "Company": FIRM_LABELS[ticker],
                        "Ticker": ticker,
                        "Fiscal year": selected_year,
                        "Status": "No score available",
                        "AI Use Score": None,
                        "Scenarios with use": None,
                        "Readiness Score": None,
                        "Talk Ratio (%)": None,
                        "Substantive passages": None,
                    }
                )
            else:
                table_rows.append(
                    {
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
                    }
                )

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
                        "They summarize categories in the score file, not verified "
                        "deployments or passage-level evidence."
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
            )
            metric_column = score_columns[selected_metric]
            trend_chart = go.Figure()
            for index, ticker in enumerate(selected_score_tickers):
                by_year = {
                    score.fiscal_year: score
                    for score in score_data
                    if score.ticker == ticker
                }
                trend_chart.add_trace(
                    go.Scatter(
                        name=FIRM_LABELS[ticker],
                        x=score_years,
                        y=[
                            getattr(by_year[year], metric_column)
                            if year in by_year
                            else None
                            for year in score_years
                        ],
                        mode="lines+markers",
                        connectgaps=False,
                        line={
                            "color": CHART_PALETTE[index % len(CHART_PALETTE)],
                            "width": 2.5,
                        },
                        marker={"size": 7},
                        hovertemplate="%{x}: %{y}<extra>%{fullData.name}</extra>",
                    )
                )
            trend_chart.update_layout(
                **chart_layout(f"Annual {selected_metric} by Firm", selected_metric)
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

with about_tab:
    st.subheader("Data Sources and Limits")
    st.markdown(
        "- Individual company scores are read from "
        "`data/processed/sec/company_scores_consensus.csv`; each row is one company–fiscal year "
        "scored from SEC 10-K and 10-Q passages.\n"
        "- **Label coverage is mixed:** 80 of 277 passages have human-agreed labels; the remaining "
        "passages use AI-draft labels. Scores are based on disclosures, not verified firm-wide "
        "AI activity.\n"
        "- The sector overview reads `data/processed/sec/sector_index.csv`. It presents both "
        "equal-weighted and market-cap-weighted scores for the six core firms; Citigroup is a "
        "benchmark and is excluded. The cap-weighted series uses public float from SEC filings.\n"
        "- “Financial sector” here means this selected six-company proof-of-concept sample "
        "(four banks, Charles Schwab, and Principal Financial Group), not every financial-services "
        "firm or a standard market-sector index.\n"
        "- FY2026 is partial and is hidden from the score views. Missing firm-years remain "
        "unavailable rather than being filled with zero.\n"
        "- Scenario codes and names follow the frozen taxonomy. The score files do not contain "
        "evidence IDs or citations, so the dashboard does not provide passage-level drill-down.\n"
        "- A score of zero means no scored use was found in the available disclosures; it does "
        "not establish that a firm does not use AI. The six-firm index is not a census of the "
        "financial-services sector."
    )
    st.markdown("### Score Definitions")
    for metric, definition in SCORE_METRIC_HELP.items():
        st.markdown(f"**{metric}.** {definition}")

st.caption(
    "SEC disclosure scores · Human-checked and AI-draft labels · "
    "Not verified firm-wide adoption or investment advice"
)
