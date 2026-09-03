# Escape Room

A beginner-friendly, text-based escape room game built with Python.

## About the Game

You find yourself trapped inside your boss's office during a dinner party at his old mansion.

The door is locked, and a 4-digit keypad stands between you and your escape.

Explore the room, examine your surroundings, discover clues, solve the puzzles, and find your way out.

## How to Play

The game is played entirely through the terminal.

You will be given a list of actions to choose from. Examine objects around the room, collect items, follow clues, and solve the puzzles to discover the final code.

Your goal is simple:

**Escape the room.**

## Requirements

* Python 3.14 or later
* Git

## Installation

Clone the repository:

```bash
git clone git@github.com:beccaschmidt/escape-room.git
```

Move into the project directory:

```bash
cd escape-room
```

Create a virtual environment:

```bash
python3 -m venv .venv
```

Activate the virtual environment:

```bash
source .venv/bin/activate
```

Install the game:

```bash
python -m pip install -e .
```

## Play the Game

Start the game with:

```bash
python -m escape_room.main
```

Follow the instructions in the terminal and try to escape.

## Playtesting

If you are testing the game for the first time, please play without looking at the source code or asking for hints.

## Development

This project is being developed as a learning and portfolio project to practise Python, Git, GitHub, testing, and software development workflows.

Features are developed on separate branches and merged into `main` through pull requests.

## Future Improvements

Planned improvements could include:

* Additional rooms and puzzles
* More interactive objects
* More complex inventory mechanics
* Additional story and character development
