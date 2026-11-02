# Number Guessing Game

A simple Python game where the computer picks a number between 1 and 100, and you try to guess it.

## How to play

- Pick a difficulty: **easy** gives you 10 tries, **hard** gives you 5.
- Type a guess. The game tells you if it's **too high** or **too low**.
- Guess the number before you run out of tries to win.

## What it does

- Picks a new random number every game
- Keeps asking until you type `easy` or `hard`
- If you type letters or leave it empty, it tells you and doesn't take away a try
- If you guess outside 1 to 100, it tells you and doesn't take away a try
- Shows the answer at the end if you lose

## How to run it

You need Python 3 installed.

```bash
python NumGuessingGame.py
```

## Example

```
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
Choose a difficulty. Type 'easy' or 'hard': easy
You have 10 attempts remaining to guess the number.
Make a guess: 50
Too high.

You have 9 attempts remaining to guess the number.
Make a guess: 25
Too low.

You have 8 attempts remaining to guess the number.
Make a guess: abc
Please enter a whole number.

You have 8 attempts remaining to guess the number.
Make a guess: 42
You got it! The answer was 42.
```

## How it works

1. The player picks a difficulty, which sets the number of tries.
2. The computer picks a random number with `random.randint(1, 100)`.
3. A `while` loop runs as long as there are tries left.
4. Each guess is checked: is it a number, is it between 1 and 100, is it right?
5. A wrong guess removes one try. A right guess ends the game.
6. If the loop ends with no tries left, the `else` part of the loop shows the answer.

## Flowchart

![Flowchart](NumGuessingGame_FlowChart.png)

There's also a PDF version: [`NumGuessingGame_FlowChart.pdf`](NumGuessingGame_FlowChart.pdf)

## What I learned

- How to use the `random` module
- How to use `try/except` so bad input doesn't crash the game
- How to use `continue` to skip the rest of a loop
- That a `while` loop can have an `else` part that runs when the loop ends normally

## Ideas for later

- Add a "Play again?" option
- Keep track of the best score (fewest tries)
- Add a medium difficulty
