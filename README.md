# Basketball Stats Tracker

A beginner-friendly Python console application for recording basketball players' points, rebounds, and assists across games. The tracker calculates each player's average stats per game.

## Features

- Add players and record stats for their first game.
- Record stats for additional games for existing players.
- View each player's number of games and average points, rebounds, and assists per game.
- Check inputs so stats must be non-negative whole numbers.
- Store data in memory for the current session.

> Player and game data is not saved to a file. It is cleared when the program exits.

## Requirements

- Python 3.6 or newer
- A terminal or command prompt
- No third-party Python packages

## Installation

1. Install Python from [python.org](https://www.python.org/downloads/) if it is not already installed. On Windows, enable the option to add Python to `PATH` during setup if available.
2. Download or clone this project to your computer.
3. Open a terminal and change to the project folder, which contains `basketball_stats.py`.

There are no additional packages to install.

## Run the Program

From the project folder, run one of these commands:

```text
python basketball_stats.py
```

On Windows, this command may also be available:

```text
py basketball_stats.py
```

## Usage Guide

When the program starts, choose an option from the menu:

1. **Add a player**: Enter a player's name and their points, rebounds, and assists for their first game.
2. **Add game stats for a player**: Choose a player by their number, then enter stats for another game.
3. **View player averages**: Display the number of games recorded and the average for each stat. Averages are shown to one decimal place.
4. **Exit**: Close the program.

Points, rebounds, and assists must each be entered as a whole number greater than or equal to zero. If an entry is invalid, the program asks again.

## Example

For example, add Maya Chen and enter `20` points, `8` rebounds, and `5` assists for her first game. Use **Add game stats for a player** to record another game with `10` points, `4` rebounds, and `3` assists. The averages will be:

```text
Maya Chen (2 games)
	Points: 15.0 | Rebounds: 6.0 | Assists: 4.0
```