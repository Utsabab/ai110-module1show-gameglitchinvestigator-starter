# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
The number guessing game lets user input number in order to guess a secret random number chosen by the program.
- List at least two concrete bugs you noticed at the start  
  1.
  What happened:
  * The range of numbers and the attempts allowed for easy, normal and hard mode are inconsistent. 
  What's expected:
  * The normal mode should have lower range of numbers than easy and lower allowed attempts than easy mode.
  2.
  What happened: 
  * The hints are incorrect. Suggests to go higher on the guess while the secret number is less than the attempted guess.
  What's expected:
  * Should advise to go higher if the current guess is less than the secret number and to go lower if the current guess is greater than the secret number.
  3.
  What happened:
  * Attempts left metric is inconsistent. The number is 1 less than the attempts allowed when the game is initially started but is restored to the correct number when the game is renewed.
  What's expected:
  * The game should show correct allowed attempts at the start of the game.
  4.
  What happened:
  * If you start new game before losing or winning the current game, the history isn't cleared. 
  What's expected:
  * The history should be cleared when the new game is started.
  5.
  What happened:
  * Can't play the game even after starting a new game if you lose or win the current game. 
  What's expected:
  * The game should be playable when the new game is started.
  6.
  What happened:
  * The attempts left counter in the game is not real time and also the game history doesn't update in real-time.
  What's expected:
  * The game history and the attempt left counter should be real-time reflecting the most recent guess made by the user.
  7.
  What happened: When the new game is started, the game ignores the range for the game level and generated secret number out of bounds.
  What's expected: Teh secret number should be generated within the range bounds of the given game level after renewing game.
  8.
  What happened: The game always displays Guess a number between 1 and 100.
  What's expected: The game should display text to ask user to guess a number between the given range of the game level. 
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
