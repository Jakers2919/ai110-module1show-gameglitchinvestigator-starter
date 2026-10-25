import json
from pathlib import Path
from unittest.mock import patch

import pytest

from streamlit.testing.v1 import AppTest

from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == ("Win", "🎉 Correct!")

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == ("Too High", "📉 Go LOWER!")

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == ("Too Low", "📈 Go HIGHER!")


def test_submitted_guesses_display_matching_hints():
    app = AppTest.from_file(str(Path(__file__).resolve().parents[1] / "app.py"))
    app.run()
    app.session_state["secret"] = 77

    for guess, message in [
        (50, "Go HIGHER!"),
        (90, "Go LOWER!"),
        (9, "Go HIGHER!"),
        (77, "Correct!"),
    ]:
        app.text_input[0].set_value(str(guess))
        app.button[0].click().run()
        assert not app.exception
        assert app.session_state["secret"] == 77
        # Streamlit may extract the leading emoji into the alert's icon.
        assert app.warning[0].value.endswith(message)

    assert app.session_state["status"] == "won"
    assert any("You won! The secret was 77." in item.value for item in app.success)


@pytest.mark.parametrize("status", ["won", "lost", "playing"])
def test_new_game_resets_round_and_accepts_guesses(status):
    app = AppTest.from_file(str(Path(__file__).resolve().parents[1] / "app.py"))
    app.run()
    app.sidebar.selectbox[0].select("Easy").run()
    app.session_state["secret"] = 17
    app.session_state["attempts"] = 5
    app.session_state["history"] = [3, 17]
    app.session_state["status"] = status
    app.session_state["score"] = 60

    with patch("random.randint", return_value=12) as generate_secret:
        app.button[1].click().run()
        generate_secret.assert_called_once_with(1, 20)

    assert not app.exception
    assert app.session_state["attempts"] == 0
    assert app.session_state["history"] == []
    assert app.session_state["status"] == "playing"
    assert app.session_state["score"] == 0
    assert app.session_state["secret"] == 12

    app.text_input[0].set_value("10")
    app.button[0].click().run()
    assert not app.exception
    assert app.session_state["attempts"] == 1
    assert app.session_state["history"] == [10]
    assert app.session_state["secret"] == 12
    assert app.warning[0].value.endswith("Go HIGHER!")


def test_debug_history_updates_on_each_submission():
    app = AppTest.from_file(str(Path(__file__).resolve().parents[1] / "app.py"))
    app.run()
    app.session_state["secret"] = 77
    history = []

    for raw_guess, recorded_guess in [("50", 50), ("90", 90), ("oops", "oops"), ("77", 77)]:
        app.text_input[0].set_value(raw_guess)
        app.button[0].click().run()
        history.append(recorded_guess)
        assert not app.exception
        assert json.loads(app.expander[0].json[0].value) == history

    # History remains visible when the finished-round guard stops the next run.
    app.run()
    assert json.loads(app.expander[0].json[0].value) == history
