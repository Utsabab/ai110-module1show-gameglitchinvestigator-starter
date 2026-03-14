# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?

  The number guessing game lets user input number in order to guess a secret random number chosen by the program.

- List at least two concrete bugs you noticed at the start:

  1. **What happened:** The range of numbers and the attempts allowed for easy, normal and hard mode are inconsistent.

     **What's expected:** The normal mode should have lower range of numbers than easy and lower allowed attempts than easy mode.

  2. **What happened:** The hints are incorrect. Suggests to go higher on the guess while the secret number is less than the attempted guess.

     **What's expected:** Should advise to go higher if the current guess is less than the secret number and to go lower if the current guess is greater than the secret number.

  3. **What happened:** Attempts left metric is inconsistent. The number is 1 less than the attempts allowed when the game is initially started but is restored to the correct number when the game is renewed.

     **What's expected:** The game should show correct allowed attempts at the start of the game.

  4. **What happened:** If you start new game before losing or winning the current game, the history isn't cleared.

     **What's expected:** The history should be cleared when the new game is started.

  5. **What happened:** Can't play the game even after starting a new game if you lose or win the current game.

     **What's expected:** The game should be playable when the new game is started.

  6. **What happened:** The attempts left counter in the game is not real time and also the game history doesn't update in real-time.

     **What's expected:** The game history and the attempt left counter should be real-time reflecting the most recent guess made by the user.

  7. **What happened:** When the new game is started, the game ignores the range for the game level and generates a secret number out of bounds.

     **What's expected:** The secret number should be generated within the range bounds of the given game level after renewing game.

  8. **What happened:** The game always displays "Guess a number between 1 and 100."

     **What's expected:** The game should display text to ask user to guess a number between the given range of the game level.
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?

  I used Claude to fix bugs within the code while used Copilot agent to refactor the code.
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).

  Among many, Claude suggested me to remove code that was converting guess instance to string and comparing it with the int of secret number which was causing the hint to be inconsistent. I verified the result by testing how hints suggest while guessing the number through different levels of the game.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

  I asked Claude to make the history of the game and attempts left counter to be real-time as it wasn't reflecting the most recent guess. Claude instead created a new history feature where it displayed the history of the game while the bug remained unfixed. I verified it by playing the game. I reprompted by outlining what we have and what needed to be fixed and Claude eventually fixed the issue and now the game shows attempts left and history in real-time as soon as the guess is made.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?

  Once the bug was fixed, I replayed the game to make sure the bug that I was dealing with was fixed through repetition. In addition, I used Claude to generate pytest testcases that tested all the bug fixes except for the one's that need UI/Integration testing.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.

  One manual test that I conducted was for Bug 7, where when the new game was started, game disregarded the range level of numbers for the given game level and generated secret number that were out of bounds. I validated the fix by playing games multiple times and also through pytest testcases.
- Did AI help you design or understand any tests? How?

  Yes. Claude helped me design testcases that precisely tested the bug fixes I made on the code. For example, when testing for Bug 1 to validate updated range of numbers for each level of the game, the testcase validated the generated secret code is within the bounds after new game is started and the upper bounds are according to the game level as well.
  In addition, Claude generated pytest testcases to test beyind our bug fixes, where it tested the function that parsed the user input with edge cases such as using float, string, and empty input and also validated the correctness of score calculation of the game.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

  Every time a user clicks on the button or changes a dropdown, the entire page refreshes, all the variables are re-created and calculations rerun. In order to not lose the progress we have made, sessions states exist which acts as a memory between reruns for a given user. Think of it as a notepad Streamlit keeps on the side.
  Rerun -> Erase everything that's written on the whiteboard.
  Session state -> Sticky note on the corner of the whiteboard that survices erasing.
  
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?

  - This could be a testing habit, a prompting strategy, or a way you used Git.
  Get hands-on with the existing codebase to see how it functions and identify evident bugs. Use AI to validate the bugs and check for any new ones. Use AI to fix the code but manually read the changes and understand how it changes the output before approving the changes.
- What is one thing you would do differently next time you work with AI on a coding task?

  I won't use AI atleast before experimenting with the app and understanding what the objective of the app is, what are some major issues that are existent in the app.
- In one or two sentences, describe how this project changed the way you think about AI generated code.

  AI generated codes can fix bugs and design implemetations very fast and can impact the speed and impact of any product/service.
