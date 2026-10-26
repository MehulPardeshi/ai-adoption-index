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

HEADING_FONT = "'Merriweather', Georgia, serif"
BODY_FONT = "'Inter', system-ui, sans-serif"
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
.stApp {{
    background: var(--dashboard-background);
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
.st-key-use_case_stack {{
    padding: 0.8rem;
    background: #EAF3FF;
    border: 1px solid #D4E5FC;
    border-radius: 0.35rem;
}}
.st-key-use_case_stack [class*="st-key-use_case_card"] {{
    padding: 0.45rem 0.55rem 1rem;
    margin-bottom: 0.45rem;
    background: var(--dashboard-surface);
    border: 1px solid var(--dashboard-border);
    border-radius: 0.35rem;
    transition: border-color 120ms ease, box-shadow 120ms ease;
}}
.st-key-use_case_stack [class*="st-key-use_case_card"]:hover {{
    border-color: #A7C8F5;
}}
.st-key-use_case_stack [class*="st-key-use_case_card_open"] {{
    border: 2px solid var(--dashboard-accent);
    box-shadow: 0 1px 4px rgba(26, 115, 232, 0.12);
}}
.st-key-use_case_stack [class*="st-key-use_case_card"] .stButton button {{
    position: relative;
    min-height: 2.5rem;
    max-height: 2.5rem;
    height: 2.5rem;
    justify-content: center;
    color: transparent !important;
    background: transparent;
    border: 0;
    padding: 0.2rem;
    font-size: 0 !important;
    box-shadow: none;
}}
.st-key-use_case_stack [class*="st-key-use_case_card"] .stButton button > div {{
    position: absolute !important;
    width: 1px !important;
    height: 1px !important;
    padding: 0 !important;
    margin: -1px !important;
    overflow: hidden !important;
    clip: rect(0, 0, 0, 0) !important;
    white-space: nowrap !important;
    border: 0 !important;
}}
.st-key-use_case_stack [class*="st-key-use_case_card"] .stButton button:hover {{
    background: #EAF3FF;
}}
.st-key-use_case_stack [class*="st-key-use_case_card"] .stButton button:focus-visible {{
    outline: 3px solid var(--dashboard-accent);
    outline-offset: 1px;
}}
.st-key-use_case_stack [class*="st-key-use_case_card"] .stButton button::after {{
    content: "";
    display: block;
    width: 0.55rem;
    height: 0.55rem;
    color: var(--dashboard-accent);
    border-right: 2px solid var(--dashboard-accent);
    border-bottom: 2px solid var(--dashboard-accent);
    transform: rotate(45deg) translate(-2px, -2px);
    transition: transform 120ms ease;
}}
.st-key-use_case_stack [class*="st-key-use_case_card_open"] .stButton button::after {{
    transform: rotate(225deg) translate(-2px, -2px);
}}
.st-key-use_case_stack [class*="st-key-use_case_card"] .stMarkdown {{
    margin: 0;
}}
.st-key-use_case_stack [class*="st-key-use_case_card"] .stHorizontalBlock [data-testid="stMarkdownContainer"] {{
    margin-bottom: 0 !important;
}}
.use-case-title {{
    color: var(--dashboard-structural);
    font-family: {BODY_FONT};
    font-size: 0.98rem;
    font-weight: 700;
    line-height: 1.35;
    text-align: left;
}}
.use-case-badge {{
    padding: 0.18rem 0.45rem;
    text-align: center;
    white-space: nowrap;
    font-family: {BODY_FONT};
    font-size: 0.76rem;
    line-height: 1.4;
    border-radius: 0.3rem;
}}
.stage-exploring {{
    color: #4D3A69;
    background: #EEE8F6;
}}
.stage-pilot {{
    color: #164F97;
    background: #DCEBFF;
}}
.stage-in_use {{
    color: #245B32;
    background: #DDF2E1;
}}
.quarter-badge {{
    color: #FFFFFF;
    background: #70A7F8;
}}
.use-case-summary {{
    padding: 0.35rem 0.45rem 0.15rem;
    color: var(--dashboard-text);
    font-size: 0.98rem;
    line-height: 1.5;
}}
.use-case-evidence {{
    box-sizing: border-box;
    max-width: 100%;
    margin: 0.3rem 0.45rem 0;
    padding: 0.55rem 0.7rem;
    color: var(--dashboard-muted);
    background: #F8FAFD;
    border-left: 3px solid var(--dashboard-border);
    font-size: 0.82rem;
    line-height: 1.45;
    overflow-wrap: anywhere;
}}
@media (max-width: 760px) {{
    .st-key-use_case_stack {{
        padding: 0.45rem;
    }}
    .use-case-badge {{
        font-size: 0.65rem;
        padding: 0.16rem 0.25rem;
    }}
}}
</style>
"""
