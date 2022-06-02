# Simple Tic-Tac-Toe

This Python-based project provides a simple implementation of the classic game Tic-tac-toe. Tic-tac-toe is a paper-and-pencil game for two players, X and O, who take turns marking the spaces in a 3x3 grid. The player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row wins the game.

## Requirements

- [Python 3](https://www.python.org/downloads/)

## Installation

This application is written in Python, so you'll need Python installed on your computer to run it. If you don't have Python installed, you can download it from [python.org](https://www.python.org/downloads/).

To install this project, clone the repository to your local machine:

```
git clone https://github.com/SonikSeven/simple-tic-tac-toe.git
```

## How to Run

To run the program, follow these steps:

1. Open a terminal and navigate to the directory where the script is located.
2. Run the script using Python:

```
python main.py
```

## How to Play

- The game will display a 3x3 grid and prompt you to enter the coordinates where you wish to place your mark (X or O).
- Coordinates are entered in the form "row column". Both row and column numbers should be between 1 and 3.
- X always goes first.
- Players take turns to input their coordinates.
- If a player tries to place their mark in an occupied spot or outside the grid, the game will notify them to pick another spot.

## Game Rules

1. The game is played on a 3x3 grid.
2. You are X, your friend is O. take turns putting their marks in empty squares.
3. The first player to get 3 of her marks in a row (up, down, across, or diagonally) is the winner.
4. When all 9 squares are full, the game is over. If no player has 3 marks in a row, the game ends in a draw.

## License

This project is licensed under the [MIT License](LICENSE.txt).
