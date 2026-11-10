import unittest

from src.dashboard.theme import (
    BODY_FONT,
    CHART_PALETTE,
    COLORS,
    HEADING_FONT,
    THEME_CSS,
    book_title,
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
        self.assertIn(
            "a:focus-visible, button:focus-visible, [role=\"combobox\"]:focus-visible",
            THEME_CSS,
        )
        self.assertIn("text-decoration: underline", THEME_CSS)

    def test_scrolling_canvas_uses_consistent_light_background(self):
        self.assertIn(
            '[data-testid="stMainBlockContainer"], main',
            THEME_CSS,
        )
        self.assertIn(
            "background-color: var(--dashboard-background) !important",
            THEME_CSS,
        )
        self.assertIn("background: var(--dashboard-surface)", THEME_CSS)

    def test_disclaimers_are_compact_and_keep_the_yellow_fyi_surface(self):
        self.assertIn(".st-key-global_disclaimer [data-testid=\"stAlert\"]", THEME_CSS)
        self.assertIn("background: #FFF8DB !important", THEME_CSS)
        self.assertIn("font-size: 0.875rem !important", THEME_CSS)
        self.assertIn("padding: 0.4rem 0.7rem !important", THEME_CSS)

    def test_book_titles_lowercase_minor_words_and_preserve_acronyms(self):
        self.assertEqual(
            book_title("cumulative records by demo quarter"),
            "Cumulative Records by Demo Quarter",
        )
        self.assertEqual(
            book_title("AI adoption in the SEC"),
            "AI Adoption in the SEC",
        )
        self.assertEqual(book_title("the use of AI"), "The Use of AI")

    def test_compare_firm_chips_use_accessible_blue(self):
        self.assertIn('[data-testid="stMultiSelect"] [data-tag]', THEME_CSS)
        self.assertIn("background-color: var(--dashboard-accent) !important", THEME_CSS)
        self.assertIn("color: #FFFFFF !important", THEME_CSS)
        self.assertIn("background: var(--dashboard-accent-hover) !important", THEME_CSS)
        self.assertIn("outline: 2px solid var(--dashboard-structural)", THEME_CSS)

    def test_sector_help_buttons_match_company_help_button_style(self):
        self.assertIn(".st-key-score_help_ai_use_score button", THEME_CSS)
        for key in (
            "sector_help_button_fiscal_year",
            "sector_help_button_firms_in_index",
            "sector_help_button_equal_weighted_score",
            "sector_help_button_market_cap_weighted_score",
            "sector_help_button_public_float_usd",
            "sector_help_fiscal_year",
            "sector_help_firms_in_index",
            "sector_help_equal_weighted_score",
            "sector_help_market_cap_weighted_score",
            "sector_help_public_float_usd",
        ):
            self.assertIn(
                f'div.st-key-{key} [data-testid="stBaseButton-secondary"]',
                THEME_CSS,
            )
        self.assertIn("width: 2rem !important", THEME_CSS)
        self.assertIn("height: 2rem !important", THEME_CSS)
        self.assertIn("border-radius: 50% !important", THEME_CSS)
        self.assertIn("color: var(--dashboard-accent) !important", THEME_CSS)
        self.assertIn(
            'div.st-key-sector_help_row [data-testid="stHorizontalBlock"]',
            THEME_CSS,
        )
        self.assertIn("flex-wrap: nowrap !important", THEME_CSS)
        self.assertIn("height: 4.5rem", THEME_CSS)

    def test_charts_use_the_theme_palette(self):
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
