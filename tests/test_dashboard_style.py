import unittest

from src.dashboard.theme import (
    BODY_FONT,
    CHART_PALETTE,
    COLORS,
    HEADING_FONT,
    STAGE_COLORS,
    THEME_CSS,
)


class DashboardStyleTests(unittest.TestCase):
    def test_palette_matches_the_visual_style_guide(self):
        self.assertEqual(COLORS["accent"], "#1A73E8")
        self.assertEqual(COLORS["accent_hover"], "#155CB8")
        self.assertEqual(COLORS["structural"], "#2E1A47")
        self.assertEqual(COLORS["background"], "#F8F9FA")
        self.assertEqual(COLORS["surface"], "#FFFFFF")
        self.assertEqual(COLORS["text"], "#202124")

    def test_font_stacks_have_local_system_fallbacks(self):
        self.assertTrue(HEADING_FONT.endswith("serif"))
        self.assertTrue(BODY_FONT.endswith("sans-serif"))
        self.assertIn("Georgia", HEADING_FONT)
        self.assertIn("system-ui", BODY_FONT)
        self.assertEqual(HEADING_FONT, "'Merriweather', Georgia, serif")
        self.assertEqual(BODY_FONT, "'Inter', system-ui, sans-serif")

    def test_css_applies_palette_minimal_edges_and_accessible_focus(self):
        self.assertIn("--dashboard-background: #F8F9FA", THEME_CSS)
        self.assertIn("--dashboard-surface: #FFFFFF", THEME_CSS)
        self.assertIn("background: var(--dashboard-surface)", THEME_CSS)
        self.assertIn('[data-testid="stHeader"]', THEME_CSS)
        self.assertIn('[data-testid="stAppViewContainer"]', THEME_CSS)
        self.assertIn('[data-testid="stMain"]', THEME_CSS)
        self.assertIn("min-height: 100vh", THEME_CSS)
        self.assertIn("position: relative !important", THEME_CSS)
        self.assertIn("background: transparent", THEME_CSS)
        self.assertIn("main h1, main h2, main h3, main h4", THEME_CSS)
        self.assertIn("font-family: 'Merriweather', Georgia, serif", THEME_CSS)
        self.assertIn("font-family: 'Inter', system-ui, sans-serif", THEME_CSS)
        self.assertIn("--font-heading: 'Merriweather', Georgia, serif", THEME_CSS)
        self.assertIn("--font-body: 'Inter', system-ui, sans-serif", THEME_CSS)
        self.assertIn("fonts.googleapis.com/css2", THEME_CSS)
        self.assertIn("border-radius: 0 !important", THEME_CSS)
        self.assertIn("outline: 3px solid var(--dashboard-accent)", THEME_CSS)
        self.assertIn(".st-key-use_case_stack", THEME_CSS)
        self.assertIn('[class*="st-key-use_case_card_open"]', THEME_CSS)
        self.assertIn("border: 2px solid var(--dashboard-accent)", THEME_CSS)
        self.assertIn(".stButton button:focus-visible", THEME_CSS)
        self.assertIn(".stage-in_use", THEME_CSS)
        self.assertIn(".quarter-badge", THEME_CSS)
        self.assertIn("text-decoration: underline", THEME_CSS)
        self.assertIn('[class*="st-key-use_case_card_open"] .stButton button::after', THEME_CSS)
        self.assertIn('content: ""', THEME_CSS)
        self.assertIn("clip: rect(0, 0, 0, 0) !important", THEME_CSS)
        self.assertIn("border-right: 2px solid var(--dashboard-accent)", THEME_CSS)
        self.assertIn('.stHorizontalBlock [data-testid="stMarkdownContainer"]', THEME_CSS)
        self.assertIn("transform: rotate(45deg)", THEME_CSS)
        self.assertIn("transform: rotate(225deg)", THEME_CSS)
        self.assertNotIn(".use-case-caret", THEME_CSS)

    def test_compare_firm_chips_use_accessible_blue(self):
        self.assertIn('[data-testid="stMultiSelect"] [data-tag]', THEME_CSS)
        self.assertIn("background-color: var(--dashboard-accent) !important", THEME_CSS)
        self.assertIn("color: #FFFFFF !important", THEME_CSS)
        self.assertIn("background: var(--dashboard-accent-hover) !important", THEME_CSS)
        self.assertIn("outline: 2px solid var(--dashboard-structural)", THEME_CSS)

    def test_evidence_preview_stays_within_card_and_wraps(self):
        self.assertIn("box-sizing: border-box", THEME_CSS)
        self.assertIn("max-width: 100%", THEME_CSS)
        self.assertIn("margin: 0.3rem 0.45rem 0", THEME_CSS)
        self.assertIn("overflow-wrap: anywhere", THEME_CSS)
        self.assertIn("padding: 0.45rem 0.55rem 1rem", THEME_CSS)

    def test_chart_stages_use_theme_colors(self):
        self.assertEqual(STAGE_COLORS["Exploring"], COLORS["structural"])
        self.assertEqual(STAGE_COLORS["Pilot"], COLORS["accent"])
        self.assertEqual(STAGE_COLORS["In use"], COLORS["chart_neutral"])
        self.assertEqual(len(CHART_PALETTE), 5)
        self.assertEqual(CHART_PALETTE[0], COLORS["structural"])
        self.assertEqual(CHART_PALETTE[1], COLORS["accent"])

    def test_text_color_pairs_meet_wcag_aa_contrast(self):
        def luminance(color):
            channels = [int(color[index:index + 2], 16) / 255 for index in (1, 3, 5)]
            linear = [
                value / 12.92 if value <= 0.04045 else ((value + 0.055) / 1.055) ** 2.4
                for value in channels
            ]
            return sum(
                channel * weight
                for channel, weight in zip(linear, (0.2126, 0.7152, 0.0722))
            )

        def contrast_ratio(foreground, background):
            lighter, darker = sorted(
                (luminance(foreground), luminance(background)), reverse=True
            )
            return (lighter + 0.05) / (darker + 0.05)

        for foreground in (
            COLORS["text"],
            COLORS["muted"],
            COLORS["structural"],
            COLORS["accent"],
        ):
            with self.subTest(foreground=foreground):
                self.assertGreaterEqual(
                    contrast_ratio(foreground, COLORS["surface"]),
                    4.5,
                )
        self.assertGreaterEqual(
            contrast_ratio(COLORS["surface"], COLORS["accent"]),
            4.5,
        )


if __name__ == "__main__":
    unittest.main()
