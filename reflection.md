# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

When I first ran the game, it looked like a normal number guessing game where you had to guess the correct number with limited attempts. One problem I noticed was that the hints were backwards. The secret number was 77, but when I guessed 50 and 25, the game told me to go lower instead of higher. This made the game confusing because following the hints would take me further away from the correct answer.  

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input Used | Expected Behavior | Actual Behavior | Console Output / Error |
|---|---|---|---|
| Guess 50 (secret 77) | GO HIGHER! | GO LOWER! | Incorrect hint displayed |
| Guess 25 (secret 77) | GO HIGHER! | GO LOWER! | Incorrect hint displayed |
| Click New Game after winning | Reset game and allow new guesses | Secret changed, but old history and win status remained; couldn't submit | "You already won" |
| Submit guess 60 | Guess should appear in history immediately after one submission | Guess did not appear in history until another submission | Delayed history update |


---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.
I used the AI assistant in VS Code to help me figure out why the guessing game was giving incorrect hints. I explained that the secret number was 77, but guessing 50 and 25 told me to go lower instead of higher. The AI looked through the code and found that the secret number was sometimes converted into a string, which caused the comparisons to work incorrectly. This helped me understand what was causing the bug instead of just guessing where the problem was. 
I also used Codex in VS Code to help fix the game and check my changes. One suggestion that worked was fixing the comparison between the guess and secret number. I tested numbers above and below the secret to make sure both hints worked correctly. At first, the hint still wasn't updating correctly, so I didn't accept the first fix as finished. I asked the AI to check how Streamlit displayed the hints and make another small change. After that, I tested both directions again and confirmed they worked.

---

## 3. Debugging and testing your fixes
I decided a bug was fixed by testing the game myself instead of just trusting that the code was changed. For example, I tested guesses above and below the secret number to check the hints. I also tested the New Game button after winning to make sure everything reset. For the history bug, I submitted two guesses and checked that both appeared immediately without duplicates. Codex also helped create and run automated tests using pytest, and all 8 tests passed. This helped me feel more confident that the fixes were working.
- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?
Streamlit reruns the Python script whenever someone interacts with the app, like clicking a button or submitting a guess. Session state is what lets the app remember information between those reruns. For example, it keeps track of the secret number, attempts, score, and previous guesses. Without session state, the game would lose that information whenever the page updated. I learned that the order of the code matters because something might display before the information gets updated.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits
One habit I want to keep using is testing my code after every change instead of waiting until the end. It made finding problems easier because I could see exactly what was working and what wasn't.
Next time I use AI for coding, I would explain the bug more clearly from the beginning and ask it to focus on one problem at a time. This project taught me that AI can be really helpful with finding and fixing bugs, but I still need to understand the changes and test the code myself instead of assuming everything it generates is correct.
- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
