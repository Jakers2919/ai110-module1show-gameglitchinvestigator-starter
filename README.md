# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

Game Purpose: The purpose of this game is to guess a randomly generated secret number. The game gives hints telling the player to guess higher or lower until they find the correct number.

Bugs Found: I found three main bugs. First, the game sometimes gave incorrect higher and lower hints. Second, the New Game button didn't reset everything properly. Third, the guess history would update one guess late.

Fixes Applied: I used AI in VS Code to help find and fix the bugs. We fixed the number comparison, corrected the New Game reset, and updated how the guess history displays. I also moved the game logic into logic_utils.py and tested the game to make sure everything worked.

## 📸 Demo Walkthrough

## 📸 Demo Walkthrough

1. Open the game using Streamlit and select a difficulty.
2. Expand Developer Debug Info to see the secret number for testing.
3. Enter a number higher than the secret and click Submit Guess. The game displays "Go LOWER!"
4. Enter a number lower than the secret. The game displays "Go HIGHER!"
5. Check the Developer Debug Info to confirm each guess appears in the history and the attempts counter updates.
6. Enter the correct secret number to win the game.
7. Click New Game to start another round. The attempts, history, and game status reset so the player can guess again.

## 🧪 Test Results

```text
python3 -m pytest -q
........                                         [100%]
8 passed in 1.71s
```
# Paste your pytest output here, e.g.:
# pytest tests/
# ========================= X passed in 0.XXs =========================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
