
---

# 🃏 Blackjack Game in Python

Welcome to a simple command-line Blackjack game built using Python! This project demonstrates core programming concepts such as functions, loops, conditionals, and list operations. It’s an interactive game that follows the classic Blackjack rules where you play against the computer.

---

## 📌 Features

* Command-line interface Blackjack game
* Follows basic Blackjack rules
* Handles Ace (11 or 1) logic to prevent busting
* Determines winner based on player and dealer hands
* Clean game loop with replay capability
* Code written in modular, reusable functions

---

## 🚀 How to Run

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/blackjack-python.git
   cd blackjack-python
   ```

2. **Run the game:**

   ```bash
   python blackjack.py
   ```

> Note: Ensure `art.py` is in the same directory (it contains ASCII art like a logo). If not available, you can comment out the import and `print(logo)` lines.

---

## 🧠 Game Logic Overview

### 🃏 Dealing Cards

* A function `deal_card()` returns a random card.
* Cards are picked from a standard Blackjack deck: `[11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]`.

### 🧮 Score Calculation

* The `calculate_score()` function sums cards in a hand.
* Ace (11) is converted to 1 if total goes over 21.
* Returns `0` if it’s a Blackjack (Ace + 10 with 2 cards).

### 🔍 Comparing Hands

* The `compare()` function determines the outcome:

  * Win, Lose, Draw
  * Special cases for Blackjack and busts

### 🔁 Game Loop

* You start with 2 cards.
* You can choose to "hit" (`y`) or "stand" (`n`).
* The dealer (computer) draws until their score is 17 or higher.
* Final scores are compared, and a winner is declared.

---

## 🧩 File Structure

```
blackjack-python/
│
├── blackjack.py       # Main game logic
├── art.py             # ASCII art (optional)
└── README.md          # This file
```

---

## ✍️ Example Gameplay

```
Your cards: [10, 7], current score: 17
Computer's first card: 6
Type 'y' to get another card, type 'n' to pass: n

Your final hand: [10, 7], final score: 17
Computer's final hand: [6, 8, 7], final score: 21
You lose 😤
```

---

## 🛠️ Requirements

* Python 3.x
* No external libraries required (uses only `random`)

---

## 📘 License

This project is open-source and available under the [MIT License](LICENSE).

---

## 🙌 Contributions

Feel free to fork the repo, open issues, or submit pull requests. Suggestions and improvements are welcome!

---


