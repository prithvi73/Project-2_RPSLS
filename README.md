# Rock Paper Scissors Lizard Spock 🖖

> "Scissors cuts Paper, Paper covers Rock, Rock crushes Lizard, Lizard poisons Spock, Spock smashes Scissors, Scissors decapitates Lizard, Lizard eats Paper, Paper disproves Spock, Spock vaporizes Rock, and as it always has, Rock crushes Scissors." — Sheldon Cooper

## 🚀 About The Project
This is a Python implementation of the extended Rock-Paper-Scissors game made famous by *The Big Bang Theory*.

I built this to practice **Data Structures** in Python. Instead of writing a massive wall of 25 `if/else` statements, I optimized the game logic using **Nested Dictionaries**. This makes the code scalable, cleaner, and much faster to read.

## 🛠️ How It Works
The core logic relies on a single "Rules Dictionary" that maps every winner to its losers and the specific verb used (e.g., "vaporizes", "crushes").

- **Language:** Python 3
- **Key Concept:** Nested Dictionaries (Hash Maps) & Input Handling

## 🎮 How to Play
1. Run the script:
   ```bash
   python main.py

   Choose your weapon by typing a number (1-5):

    1: Rock 🪨

    2: Paper 📄

    3: Scissors ✂️

    4: Lizard 🦎

    5: Spock 🖖

See if you can beat the computer!

🧠 Code Highlight

The "Magic" that saved me from writing 50 lines of code:
# Checking the win condition in one line using a dictionary lookup
elif comp_choice in game_rules[user_choice]:
    verb = game_rules[user_choice][comp_choice]
    print(f"You WIN as {user_choice} {verb} {comp_choice}!")
    
Created by Prithvi
