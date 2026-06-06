import unittest

from classic_session_persistence import (
    build_classic_session_snapshot,
    classic_storage_key,
    describe_classic_session_snapshot,
    validate_classic_session_snapshot,
)


def vocab_question():
    return {
        "group_id": "noun-1",
        "pos": "noun",
        "stages": ["beginner"],
        "prompt": "akvo",
        "answer_index": 1,
        "options": [
            {"japanese": "火", "esperanto": "fajro", "audio_key": "fajro"},
            {"japanese": "水", "esperanto": "akvo", "audio_key": "akvo"},
        ],
    }


def sentence_question():
    return {
        "prompt_eo": "Mi lernas Esperanton.",
        "prompt_ja": "私はエスペラントを学んでいます。",
        "answer_index": 3,
        "options": [
            {"phrase": "Li trinkas akvon.", "japanese": "彼は水を飲みます。", "level": 1, "phrase_id": "1"},
            {"phrase": "Sxi legas libron.", "japanese": "彼女は本を読みます。", "level": 2, "phrase_id": "2"},
            {"phrase": "Ni iras hejmen.", "japanese": "私たちは家へ行きます。", "level": 3, "phrase_id": "3"},
            {
                "phrase": "Mi lernas Esperanton.",
                "japanese": "私はエスペラントを学んでいます。",
                "level": 1,
                "phrase_id": "4",
            },
        ],
    }


class ClassicSessionPersistenceTests(unittest.TestCase):
    def test_vocab_snapshot_keeps_quiz_state_without_score_sync_state(self):
        snapshot = build_classic_session_snapshot(
            "vocab",
            "ja",
            {
                "questions": [vocab_question()],
                "q_index": 0,
                "correct": 0,
                "answers": [{"q_idx": 0, "selected": 0, "correct": 1, "phase": "main"}],
                "main_points": 12.5,
                "spartan_points": 0.0,
                "spartan_pending": [0],
                "spartan_mode": True,
                "quiz_direction": "eo_to_ja",
                "user_name": "TestUser",
                "group_id": "noun-1",
                "seed": 7,
                "score_saved": True,
                "pending_save_id": "must-not-persist",
                "cached_scores": [{"user": "someone"}],
            },
        )

        self.assertIsNotNone(snapshot)
        state = snapshot["state"]
        self.assertEqual(state["questions"], [vocab_question()])
        self.assertEqual(state["answers"][0]["phase"], "main")
        self.assertEqual(state["main_points"], 12.5)
        self.assertNotIn("score_saved", state)
        self.assertNotIn("pending_save_id", state)
        self.assertNotIn("cached_scores", state)
        self.assertIn("単語クイズ", describe_classic_session_snapshot(snapshot))

    def test_validation_rejects_wrong_app_or_corrupt_questions(self):
        snapshot = build_classic_session_snapshot(
            "vocab",
            "ja",
            {"questions": [vocab_question()], "q_index": 0},
        )
        wrong_app = dict(snapshot)
        wrong_app["appKind"] = "sentence"

        self.assertIsNone(
            validate_classic_session_snapshot(
                wrong_app,
                expected_app_kind="vocab",
                expected_target_lang="ja",
            )
        )

        corrupt = dict(snapshot)
        corrupt["state"] = dict(snapshot["state"])
        corrupt["state"]["questions"] = [{"prompt": "akvo", "options": []}]
        self.assertIsNone(
            validate_classic_session_snapshot(
                corrupt,
                expected_app_kind="vocab",
                expected_target_lang="ja",
            )
        )

    def test_sentence_snapshot_sanitizes_bounds_and_settings(self):
        snapshot = build_classic_session_snapshot(
            "sentence",
            "ja",
            {
                "questions": [sentence_question()],
                "q_index": 99,
                "correct": 99,
                "points_raw": 40.0,
                "points_main": 30.0,
                "points_spartan_raw": 10.0,
                "points_spartan_scaled": 5.0,
                "spartan_pending": [0, 0, 20],
                "spartan_current_q_idx": 20,
                "quiz_levels": [1, 2, 2, 99, "bad"],
                "direction": "bad",
                "sentence_user_name": "Learner",
            },
        )

        self.assertIsNotNone(snapshot)
        state = snapshot["state"]
        self.assertEqual(state["q_index"], 1)
        self.assertEqual(state["correct"], 1)
        self.assertEqual(state["spartan_pending"], [0])
        self.assertIsNone(state["spartan_current_q_idx"])
        self.assertEqual(state["quiz_levels"], [1, 2, 10])
        self.assertEqual(state["direction"], "ja_to_eo")
        self.assertIn("例文クイズ", describe_classic_session_snapshot(snapshot))

    def test_storage_keys_are_separated_by_language_and_mode(self):
        self.assertEqual(
            classic_storage_key("vocab", "ja"),
            "esperanto-choice-classic:ja:vocab:session:v1",
        )
        self.assertEqual(
            classic_storage_key("vocab", "zh"),
            "esperanto-choice-classic:zh:vocab:session:v1",
        )
        self.assertEqual(
            classic_storage_key("sentence", "ko"),
            "esperanto-choice-classic:ko:sentence:session:v1",
        )

    def test_localized_descriptions_follow_snapshot_language(self):
        zh_snapshot = build_classic_session_snapshot(
            "vocab",
            "zh",
            {"questions": [vocab_question()], "q_index": 0, "user_name": "Learner"},
        )
        ko_snapshot = build_classic_session_snapshot(
            "sentence",
            "ko",
            {"questions": [sentence_question()], "q_index": 0, "sentence_user_name": "Learner"},
        )

        self.assertIsNotNone(zh_snapshot)
        self.assertIsNotNone(ko_snapshot)
        self.assertIn("单词测验", describe_classic_session_snapshot(zh_snapshot))
        self.assertIn("用户: Learner", describe_classic_session_snapshot(zh_snapshot))
        self.assertIn("예문 퀴즈", describe_classic_session_snapshot(ko_snapshot))
        self.assertIn("사용자: Learner", describe_classic_session_snapshot(ko_snapshot))


if __name__ == "__main__":
    unittest.main()
