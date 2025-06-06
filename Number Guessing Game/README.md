# 🎲 Number-Guessing Game (CLI)

A simple command-line game where you try to guess a secretly chosen number between **1 and 100** before you run out of attempts. Great for beginners who want to practice Python basics such as loops, conditionals, user input, and the `random` module.

---

## How to Play

1. **Run the script**

   ```bash
   python guess.py
````

2. **Pick a difficulty**

   | Difficulty | Attempts |
   | ---------- | -------- |
   | `easy`     | 10       |
   | `hard`     | 5        |

3. **Start guessing**
   After each guess the program tells you whether your number is **“Too High”** or **“Too Low.”**
   Keep going until you either guess the correct number or run out of attempts.

---

## Code Walk-Through

| Section                                                 | What It Does                                                                                     |
| ------------------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| `random_num = random.randrange(1, 101)`                 | Randomly picks the secret number (upper bound is exclusive, so this covers 1-100).               |
| `difficulty = input(...)`                               | Lets the player choose their difficulty. Anything other than `"easy"` defaults to **hard mode**. |
| `life = 10` / `life = 5`                                | Sets the remaining attempts based on the chosen difficulty.                                      |
| `while game:` loop                                      | Repeats until the player wins or runs out of attempts.                                           |
| `guess = int(input(...))`                               | Reads and converts the player’s guess to an integer.                                             |
| **Comparison logic**                                    | • `guess > random_num` ➜ “Too High”                                                              |
| • `guess < random_num` ➜ “Too Low”                      |                                                                                                  |
| • `guess == random_num` ➜ Victory message and loop ends |                                                                                                  |
| `life -= 1`                                             | Decreases remaining attempts after an incorrect guess.                                           |
| `life == 0`                                             | When attempts hit zero, prints a game-over message and exits the loop.                           |

---

## Why This Is a Good Beginner Project

* **Core Python concepts** – variables, loops, conditionals, functions (if you choose to refactor).
* **User interaction** – learn to handle input safely and give clear feedback.
* **Randomness** – explore the `random` module.
* **Simple to extend** – you can add replay support, scoring, input validation, or even a GUI later.

---

## Possible Enhancements

| Idea                 | Hint                                                                                            |
| -------------------- | ----------------------------------------------------------------------------------------------- |
| **Replay option**    | Wrap gameplay in a function and ask if the user wants to play again.                            |
| **Input validation** | Catch `ValueError` if the user types something that isn’t a number.                             |
| **ASCII art**        | Already using the `art` package – try different banners or animations.                          |
| **Unit tests**       | Separate the logic for easier testing (e.g., inject the random number for deterministic tests). |

---

### License

MIT – do whatever you like, just keep the copyright and license notice. Enjoy!

```

---

### How to use this

1. Rename your script (e.g., `guess.py`) if needed.  
2. Save the block above as **README.md** (or merge it into your existing README).  
3. Commit & push – you’re done!

Happy coding, and good luck with your project!
```
