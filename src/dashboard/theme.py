"""Executable visual theme for the dashboard prototype."""

import re


COLORS = {
    "accent": "#1A73E8",
    "accent_hover": "#155CB8",
    "structural": "#2E1A47",
    "background": "#F8F9FA",
    "surface": "#FFFFFF",
    "text": "#202124",
    "muted": "#5F6368",
    "border": "#DADCE0",
    "chart_neutral": "#68707A",
    "chart_purple": "#725A8F",
    "chart_blue": "#4F8EDC",
}

HEADING_FONT = "'Merriweather', Georgia, serif"
BODY_FONT = "'Inter', system-ui, sans-serif"
CHART_PALETTE = (
    COLORS["structural"],
    COLORS["accent"],
    COLORS["chart_neutral"],
    COLORS["chart_purple"],
    COLORS["chart_blue"],
)

_LOWERCASE_TITLE_WORDS = {
    "a",
    "an",
    "and",
    "as",
    "at",
    "but",
    "by",
    "for",
    "from",
    "in",
    "nor",
    "of",
    "on",
    "or",
    "the",
    "to",
    "with",
    "yet",
}


def book_title(text: str) -> str:
    """Apply book-style capitalization while preserving acronyms and names."""
    words = list(re.finditer(r"[A-Za-z0-9]+", text))
    if not words:
        return text

    result = text
    for index in reversed(range(len(words))):
        match = words[index]
        word = match.group()
        if (
            index not in (0, len(words) - 1)
            and word.lower() in _LOWERCASE_TITLE_WORDS
        ):
            replacement = word.lower()
        elif word.isupper():
            replacement = word
        else:
            replacement = word[0].upper() + word[1:]
        result = result[:match.start()] + replacement + result[match.end():]
    return result


THEME_CSS = f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Merriweather:wght@600;700&display=swap');
:root {{
    --font-heading: {HEADING_FONT};
    --font-body: {BODY_FONT};
    --dashboard-accent: {COLORS["accent"]};
    --dashboard-accent-hover: {COLORS["accent_hover"]};
    --dashboard-structural: {COLORS["structural"]};
    --dashboard-background: {COLORS["background"]};
    --dashboard-surface: {COLORS["surface"]};
    --dashboard-text: {COLORS["text"]};
    --dashboard-muted: {COLORS["muted"]};
    --dashboard-border: {COLORS["border"]};
}}
html, body, [class*="css"] {{
    font-family: {BODY_FONT};
    color: var(--dashboard-text);
}}
html, body, #root, [data-testid="stAppViewContainer"],
[data-testid="stMain"], [data-testid="stMainBlockContainer"], main {{
    background-color: var(--dashboard-background) !important;
}}
.stApp {{
    background: var(--dashboard-background) !important;
    color: var(--dashboard-text);
    position: relative !important;
    height: auto !important;
    min-height: 100vh;
    overflow: visible !important;
}}
[data-testid="stAppViewContainer"] {{
    position: relative !important;
    height: auto !important;
    min-height: 100vh;
    overflow: visible !important;
}}
[data-testid="stMain"] {{
    height: auto !important;
    overflow: visible !important;
}}
[data-testid="stHeader"] {{
    position: relative !important;
    background: transparent;
}}
[data-testid="stSidebar"] {{
    background: var(--dashboard-background);
    border-right: 1px solid var(--dashboard-border);
}}
[data-testid="stMainBlockContainer"] {{
    max-width: 1180px;
    padding-top: 1.8rem;
    padding-bottom: 2.5rem;
}}
main h1, main h2, main h3, main h4 {{
    color: var(--dashboard-structural) !important;
    font-family: {HEADING_FONT} !important;
    letter-spacing: -0.015em !important;
    font-weight: 700 !important;
}}
main h1 {{ font-size: 2.35rem; line-height: 1.15; }}
main h2 {{ font-size: 1.55rem; }}
main h3 {{ font-size: 1.15rem; }}
main h4 {{ font-size: 1rem; }}
main p, main li, main label, main button, main input,
[data-testid="stSidebar"] p, [data-testid="stSidebar"] label,
[data-testid="stSidebar"] button {{
    font-family: {BODY_FONT} !important;
}}
main p, main li, main label, [data-testid="stSidebar"] p,
[data-testid="stSidebar"] label {{
    color: var(--dashboard-text);
}}
.eyebrow {{
    color: var(--dashboard-structural);
    font-size: 0.72rem;
    font-weight: 700;
    letter-spacing: 0.1em;
    text-transform: uppercase;
}}
[data-testid="stMetric"] {{
    background: var(--dashboard-surface);
    border: 1px solid var(--dashboard-border);
    padding: 0.75rem 0.9rem;
    border-radius: 0 !important;
}}
[data-testid="stMetricLabel"] {{ color: var(--dashboard-muted); }}
[data-testid="stMetricValue"] {{ color: var(--dashboard-text); }}
div[data-testid="stSelectbox"] label,
div[data-testid="stMultiSelect"] label {{
    color: var(--dashboard-text);
    font-weight: 600;
}}
[data-testid="stMultiSelect"] [data-tag] {{
    background-color: var(--dashboard-accent) !important;
    color: #FFFFFF !important;
    border: 1px solid var(--dashboard-accent);
    border-radius: 0.25rem !important;
}}
[data-testid="stMultiSelect"] [data-tag] > span {{
    color: #FFFFFF !important;
}}
[data-testid="stMultiSelect"] [data-tag] button {{
    color: #FFFFFF !important;
    background: transparent !important;
}}
[data-testid="stMultiSelect"] [data-tag] button:hover {{
    background: var(--dashboard-accent-hover) !important;
}}
[data-testid="stMultiSelect"] [data-tag]:focus-visible {{
    outline: 2px solid var(--dashboard-structural);
    outline-offset: 2px;
}}
a, a:visited {{
    color: var(--dashboard-accent);
    text-decoration: underline;
    text-underline-offset: 0.15em;
}}
a:focus-visible, button:focus-visible, [role="combobox"]:focus-visible {{
    outline: 3px solid var(--dashboard-accent);
    outline-offset: 2px;
}}
.stButton > button {{
    color: var(--dashboard-structural);
    background: var(--dashboard-surface);
    border: 1px solid var(--dashboard-border);
    border-radius: 0.3rem !important;
    font-weight: 600;
}}
.stButton > button:hover {{
    color: var(--dashboard-structural);
    background: #F4F8FF;
    border-color: var(--dashboard-accent);
}}
.st-key-global_disclaimer [data-testid="stAlert"] {{
    background: #FFF8DB !important;
    padding: 0.4rem 0.7rem !important;
}}
.st-key-global_disclaimer [data-testid="stAlert"] p {{
    font-size: 0.875rem !important;
    line-height: 1.4 !important;
    margin: 0.1rem 0 !important;
}}
.st-key-score_help_ai_use_score button,
.st-key-score_help_readiness_score button,
.st-key-score_help_talk_ratio button,
div.st-key-sector_help_row [data-testid="stBaseButton-secondary"],
div.st-key-sector_help_button_fiscal_year [data-testid="stBaseButton-secondary"],
div.st-key-sector_help_button_firms_in_index [data-testid="stBaseButton-secondary"],
div.st-key-sector_help_button_equal_weighted_score [data-testid="stBaseButton-secondary"],
div.st-key-sector_help_button_market_cap_weighted_score [data-testid="stBaseButton-secondary"],
div.st-key-sector_help_button_public_float_usd [data-testid="stBaseButton-secondary"],
div.st-key-sector_help_fiscal_year [data-testid="stBaseButton-secondary"],
div.st-key-sector_help_firms_in_index [data-testid="stBaseButton-secondary"],
div.st-key-sector_help_equal_weighted_score [data-testid="stBaseButton-secondary"],
div.st-key-sector_help_market_cap_weighted_score [data-testid="stBaseButton-secondary"],
div.st-key-sector_help_public_float_usd [data-testid="stBaseButton-secondary"] {{
    width: 2rem !important;
    min-width: 2rem !important;
    height: 2rem !important;
    min-height: 2rem !important;
    padding: 0 !important;
    border-radius: 50% !important;
    color: var(--dashboard-accent) !important;
    border: 1px solid var(--dashboard-accent) !important;
    background: var(--dashboard-surface) !important;
    font-size: 1rem !important;
    line-height: 1 !important;
}}
.sector-help-heading {{
    height: 4.5rem;
    display: flex;
    align-items: flex-end;
    line-height: 1.25;
    padding-bottom: 0.3rem;
}}
div.st-key-sector_help_row [data-testid="stHorizontalBlock"] {{
    flex-wrap: nowrap !important;
    align-items: flex-start !important;
}}
div.st-key-sector_help_row [data-testid="stColumn"] {{
    flex: 1 1 0 !important;
    width: 0 !important;
    min-width: 0 !important;
}}
div[data-testid="stTabs"] button[aria-selected="true"] {{
    color: var(--dashboard-structural);
    border-bottom-color: var(--dashboard-accent);
}}
div[data-testid="stAlert"],
[data-baseweb="select"], [data-baseweb="select"] *,
[data-baseweb="popover"], [data-baseweb="popover"] *,
[data-testid="stDataFrame"] {{
    border-radius: 0 !important;
}}
div[data-testid="stAlert"] {{
    background: var(--dashboard-surface);
    border: 1px solid var(--dashboard-border);
}}
[data-testid="stDataFrame"] {{
    background: var(--dashboard-surface);
    border: 1px solid var(--dashboard-border);
}}
</style>
"""
