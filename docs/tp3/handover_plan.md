# Handover plan for Julie (#142)

> **Owners:** Shu + Snehal (#142) · Mehul: public repo (#190). **Status:** plan v1, Nov 24. Based on Dr. Chung's handoff expectations (Nov 23, [minutes](../../meetings/2026-11-23-advisor.md)) and Julie's Nov 10 ask (at least a deployed link + user guide).

## What Julie gets
| # | Item | Owner | Due | Status |
|---|---|---|---|---|
| 1 | **Live dashboard** link: https://ai-adoption-index.streamlit.app (76-firm index as the headline, #134) | Yen-Chu (index on the dashboard) | Sun Nov 29 | live ✅ / 76-firm view pending |
| 2 | **User guide** `docs/user_guide.md`: open the dashboard, read a score, what the levels mean, download the CSVs (Snehal); refresh the data each year with the skill folder (Shu) | Snehal + Shu | Sun Nov 29 | to do |
| 3 | **Public final-product repo** (code, skill folder, final data, README report, user guide; no team admin files). Dr. Chung added to GitHub | Shu (file list) → Mehul (creates it) | list Sun Nov 29 · repo Wed Dec 2 | to do (#190) |
| 4 | **Skill folder** `skills/ai-adoption-index/SKILL.md`: the yearly refresh routine (about an hour, under $1) | Shu reviews → Mehul | Sun Nov 29 | draft v0.3 ✅ |
| 5 | **Recording** of the walkthrough + demo (her copy) | Shu | Tue Dec 1 (demo) · Dec 3 (Zoom) | to do (#140) |
| 6 | **Research comparison** (Babina, Dong, Evident AI) she asked for on Nov 10 | Logan | Sun Nov 29 | to do (#137) |

## The handover meeting: Thu Dec 3, 10 am, Zoom (#191)
Snehal sends the invite; Shu records. About 30 minutes:
1. **5 min** Result: FY2025 index 8.6 equal / 10.2 cap-weighted; talk ≠ use (Snehal)
2. **10 min** Live dashboard: firm drill-down, method page, CSV download (Snehal / Yen-Chu)
3. **5 min** How we checked it: overclaim bar, human review, round 3 (Mehul)
4. **5 min** How to refresh it next year: skill folder + user guide (Shu)
5. **5 min** Her questions; send the links and the recording in a follow-up email (Snehal)

## Decided
- Data stays as CSVs in the repo (no database); refresh is manual, once a year, with the skill folder.
- No paid services: Streamlit Community Cloud (free) and DeepSeek at about $0.02 per run, run on the user's own API key.
