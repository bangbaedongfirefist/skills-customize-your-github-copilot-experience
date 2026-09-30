# 📘 Assignment: Games in Python

## 🎯 Objective

Build a classic Hangman game in Python using strings, loops, conditionals, and random selection. This assignment helps students practice handling user input, tracking game state, and updating the game board as letters are guessed.

## 📝 Tasks

### 🛠️ Create the Word Selection Logic

#### Description
Set up the game so it chooses a random word from a predefined list and stores it in a variable for the player to guess.

#### Requirements
Completed program should:

- Define a list of words such as `['python', 'hangman', 'challenge', 'programming', 'computer']`
- Randomly choose one secret word from the list
- Store the selected word so it can be used throughout the game

### 🛠️ Track the Game State

#### Description
Initialize the variables needed to track the current word progress, guessed letters, and the number of incorrect guesses.

#### Requirements
Completed program should:

- Create an empty or masked version of the word to show progress, such as `_ _ _ _ _`
- Keep track of letters already guessed
- Track how many incorrect guesses have been made
- Set a maximum number of incorrect guesses, such as 6

### 🛠️ Build the Main Game Loop

#### Description
Use a loop to repeatedly ask the player for a letter, check whether it is in the hidden word, and update the game status until the game ends.

#### Requirements
Completed program should:

- Prompt the user for a letter guess
- Check whether the letter is in the secret word
- Reveal matching letters in the hidden word display
- Increase the wrong guess count when the letter is not in the word
- Display the current progress after each turn
- End the game when the player correctly guesses the word or reaches the maximum wrong guesses
- Print a clear win or lose message at the end
