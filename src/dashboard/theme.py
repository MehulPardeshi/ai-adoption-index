"""Executable visual theme for the dashboard prototype."""

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

HEADING_FONT = "Merriweather, Georgia, Cambria, serif"
BODY_FONT = '"Inter", "Helvetica Neue", Arial, sans-serif'
CHART_PALETTE = (
    COLORS["structural"],
    COLORS["accent"],
    COLORS["chart_neutral"],
    COLORS["chart_purple"],
    COLORS["chart_blue"],
)

STAGE_COLORS = {
    "Exploring": COLORS["structural"],
    "Pilot": COLORS["accent"],
    "In use": COLORS["chart_neutral"],
}

THEME_CSS = f"""
<style>
:root {{
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
.stApp {{
    background: var(--dashboard-background);
    color: var(--dashboard-text);
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
    color: var(--dashboard-surface);
    background: var(--dashboard-accent);
    border: 1px solid var(--dashboard-accent);
    border-radius: 0 !important;
    font-weight: 600;
}}
.stButton > button:hover {{
    color: var(--dashboard-surface);
    background: var(--dashboard-accent-hover);
    border-color: var(--dashboard-accent-hover);
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
