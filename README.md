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

- [ ] Describe the game's purpose.

      The purpose of the game is to create a secret number and let the user make a guess. Help user with hints to make a correct guess. There are levels to the game such as easy, medium, and hard. Each level is incrementaly hard with more range of numbers to guess from and less number of attempts.
- [ ] Detail which bugs you found.

      I found five bugs initially and added 2 more with Claude's suggestion.
      1. The range of number for each game level and number of attempts given were inconsistent.
      2. The hints were not consistent suggesting users to go higher on a guess while the correct answer is lower than the guess made.
      3. Attempts left metric was inconsistent which showed one less attempt than given when the game started initially.
      4. The history of the previos game wasn't cleared after the game was renewed.
      5. Game was unplayable after restarting after winning or losing the game.
      6. The attempts left counter and history were not real-time and created confusion.
      7. The game ignored the number range of the game level when the new game was started.
      8. The displayed text always asked the user to Guess number between 1 to 100 regardless of the game level.

- [ ] Explain what fixes you applied.

      1. The range of number for each game level was adjusted.
      2. The used input when compared with the correct answer was first converted to string, hence, producing incorrect hints, so fixed that issue by removing unwanted string conversion and using session state.
      3. Initialized the beginning attempts left count to 0.
      4. The history is cleared everytime a new game is started.
      5. The game is still playable after restarting the game.
      6. The attempts left counter and histiry was fixed to be real-time based on the recent user input.
      7. The game took into consideration the lower and higher bound of the given game level when game is restarted.
      8. The display is updated to match the lower and upper bound of the given game level.

## 📸 Demo

- [ ] ![Final demo](/Users/utsab06/Desktop/Codepath AI110/ai110-module1show-gameglitchinvestigator-starter/imagefinaldemo.jpg?raw=true)

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
