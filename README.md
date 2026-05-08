# ✊🖐️✌️ Rock-Paper-Scissors Bot

A Python-based interactive game that pits a human player against an AI opponent. This project demonstrates fundamental programming patterns used in game development and automated decision-making.

## Overview
This script implements the classic "Rock-Paper-Scissors" logic within a continuous loop. It handles user input, generates random computer moves, and maintains a running score for both competitors.

## Key Features
- **Randomized AI**: Uses the `random` library to ensure the computer's moves are unpredictable.
- **Score Tracking**: Persistent variables monitor the score across multiple rounds.
- **Input Validation**: Detects invalid entries to ensure a smooth user experience.
- **Game Loop**: An infinite `while` loop allows for continuous play until the user decides to quit.

## Technical Concepts
- **Conditional Logic**: Complex `if/elif/else` structures to determine the winner based on the game's rules.
- **User Interaction**: Implementation of `input()` and formatted strings (f-strings) for dynamic feedback.
- **Control Flow**: Use of `break` to exit the loop based on user choice.
- **String Manipulation**: Normalizing input using `.lower()` to prevent case-sensitivity errors.
