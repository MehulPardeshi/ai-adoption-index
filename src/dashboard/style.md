# Dashboard visual style guide

This guide defines the visual direction for the Streamlit dashboard prototype. It is a
maintainable starting point, not a claim that the dashboard is a finished research product.
The executable color tokens, font stacks, chart palette, and Streamlit CSS live in
[`theme.py`](./theme.py); the app imports them rather than maintaining a second theme.

## Design intent

- **Professional and research-oriented:** clear hierarchy, restrained color, readable tables.
- **Minimalist, with straight edges:** use square corners and thin borders, not rounded cards.
- **Explain the story:** visual hierarchy should make the selected firm, fictional records,
  record details, and cross-firm comparison easy to follow.
- **Demo-only boundary:** styling must not make invented examples look like verified findings.

## Color tokens

| Role | Color | Use |
|---|---|---|
| Primary accent | `#1A73E8` | Interactive controls, active states, links, focus rings, and chart emphasis |
| Accent hover | `#155CB8` | Hover state for accent buttons |
| Structural purple | `#2E1A47` | Headings and structural hierarchy |
| Page background | `#F8F9FA` | Page and sidebar foundation |
| Surface | `#FFFFFF` | Metrics, tables, and alert surfaces placed on the page background |
| Body text | `#202124` | Paragraphs, labels, and table content |
| Muted text | `#5F6368` | Secondary information and metric labels |
| Border | `#DADCE0` | Quiet dividers and component boundaries |
| Chart neutral | `#68707A` | Neutral data series; use alongside purple and blue |
| Chart purple | `#725A8F` | Additional categorical chart series |
| Chart blue | `#4F8EDC` | Additional categorical chart series |

Use the 60-30-10 idea as a restraint principle, not a literal measurement: neutrals dominate,
surfaces separate content, and accent colors draw attention only to relevant interactions or data.
Do not use accent blue as ordinary static body copy. Links are interactive, underlined, and use
the blue token; body text remains charcoal.

## Typography

- **Headings:** `'Merriweather', Georgia, serif`, bold, in structural purple.
- **Body and data:** `'Inter', system-ui, sans-serif`.
- The app loads Merriweather and Inter from Google Fonts. If the font request is unavailable,
  the browser uses the local Georgia and system sans-serif fallbacks. This is a typography-only
  network request; the demo still has no external data, model, or research connections.
- Use the sans-serif stack for paragraphs, controls, tables, captions, and data labels.

## Layout and components

- Prefer open whitespace, clear section numbering, consistent alignment, and thin straight borders.
- Keep surfaces white against the off-white background; avoid shadows and rounded card treatments.
- Keep interactive components visibly distinct and keyboard focus easy to see.
- Keep Streamlit's top toolbar controls available, but give the toolbar a transparent
  background and let the app use normal document scrolling so the toolbar scrolls away with
  the page instead of appearing as a persistent white strip.
- Selected firm chips in the comparison multi-select use the dashboard blue accent with white,
  high-contrast labels and visible remove controls.
- Present fictional use cases as independently expandable cards rather than a record table
  plus a second selector. Use a pale-blue stack behind individual white cards. Each card
  header has a left-aligned title and vertically centered stage and quarter badges, with a
  single blue dropdown control on the right. Expanded cards get a stronger blue outline and
  show the example area, fictional summary/detail, and no-source notice. Keep the evidence
  preview within the card bounds and allow its copy to wrap on narrow screens. Cards remain
  independently openable and the most recent starts open.
- Tables should prioritize concise labels, clear column headings, and readable body text.
- Charts use the executable palette in `theme.py`; label every series and describe demo counts as
  fictional records, never as actual company adoption or performance.
- Timeline lines represent cumulative counts of fictional fixture records only. Label both the
  axis and chart description so they cannot be mistaken for adoption or performance trends.
- Keep visible demo disclaimers and evidence limitations prominent throughout the journey.

## Streamlit implementation notes

The Tailwind examples in the proposal are design references only. This app uses Streamlit and
Plotly, so implement the same intent using the CSS in `theme.py`, Streamlit components, and Plotly
layout settings; do not add Tailwind as a dependency.

The guide's colors and rules are implemented in `theme.py` and imported by `app.py`. Focused
tests in `tests/test_dashboard_style.py` check the key palette and typography contracts.
