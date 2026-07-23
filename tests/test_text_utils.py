import unittest

from core.intents import Intent, RouteResult, is_personal_memory_candidate
from utils.text_utils import normalize_command, remove_wake_word


class TextUtilsTests(unittest.TestCase):
    def test_remove_wake_word_accepts_common_greetings(self):
        self.assertEqual(remove_wake_word("Hey Jarvis, open YouTube"), "open YouTube")
        self.assertEqual(remove_wake_word("jarvis what time is it"), "what time is it")

    def test_normalize_command_keeps_meaningful_words(self):
        self.assertEqual(
            normalize_command("Could you please open the calculator?"),
            "open calculator",
        )

    def test_normalize_command_does_not_remove_words_inside_other_words(self):
        self.assertEqual(
            normalize_command("search python tutorial"),
            "search python tutorial",
        )

    def test_route_result_keeps_an_observable_intent(self):
        result = RouteResult(Intent.BROWSER, "open github")
        self.assertEqual(result.intent, Intent.BROWSER)
        self.assertEqual(result.normalized_command, "open github")

    def test_only_personal_claims_are_memory_candidates(self):
        self.assertTrue(is_personal_memory_candidate("I live in Mumbai"))
        self.assertTrue(is_personal_memory_candidate("my favorite editor is VS Code"))
        self.assertFalse(is_personal_memory_candidate("what is Python"))
