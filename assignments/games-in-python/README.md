# 📘 Assignment: Games in Python

## 🎯 Objective

Create a playable Hangman game in Python that uses user input, strings, loops, conditionals, and random selection. This assignment helps students practice tracking game state, updating the display, and ending the game when the player wins or loses.

## 📝 Tasks

### 🛠️ Word Selection Logic

#### Description
Set up a list of possible words and choose one secret word at random for the player to guess.

#### Requirements
Completed program should:

- Define a list of words such as `['python', 'hangman', 'challenge', 'programming', 'computer']`
- Randomly select one secret word from the list
- Store the chosen word so it can be used throughout the game

### 🛠️ Game State Tracking

#### Description
Create the variables needed to track the hidden word, guessed letters, and the number of incorrect attempts.

#### Requirements
Completed program should:

- Show the hidden word as blanks or masked characters such as `_ _ _ _ _`
- Track which letters have already been guessed
- Count the number of incorrect guesses made by the player
- Set a maximum number of wrong guesses, such as 6

### 🛠️ Main Game Loop

#### Description
Use a loop to keep asking the player for a letter, check whether it is in the hidden word, and update the game until it ends.

#### Requirements
Completed program should:

- Prompt the user to enter a letter guess
- Check whether the guessed letter is in the secret word
- Reveal matching letters in the display when correct
- Increase the wrong guess count when the letter is not in the word
- Display the current game state after each turn
- End the game when the player solves the word or reaches the maximum number of wrong guesses
- Print a clear win or lose message at the end
