## 🧮 Simple Terminal Calculator

This little Python script lets you do quick, **continuous calculations** right from the terminal.
It supports the four basic arithmetic operations and allows you to “chain” results without restarting the program.

---

### How it works

| Section                  | Purpose                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Function definitions** | `add`, `subtract`, `multiply`, and `divide` each take two numbers and return the result.                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| **`operations` dict**    | Maps a symbol (`"+"`, `"-"`, `"*"`, `"/"`) to the corresponding function, so we can call them dynamically.                                                                                                                                                                                                                                                                                                                                                                                                                              |
| **`calculator()`**       | 1. Shows an ASCII-art logo from the separate `art` module.<br>2. Prompts for the first number.<br>3. Enters a `while`-loop that:<br>  - Lists the four operation symbols.<br>  - Asks the user to pick one.<br>  - Prompts for the next number.<br>  - Looks up and calls the proper function via `operations`.<br>  - Prints the calculation and result.<br>  - Lets the user press **`y`** to keep going with the current answer, or **`n`** to clear the screen (20 newlines) and start fresh by recursively calling `calculator()`. |
| **Tail call**            | After the outer loop breaks, we print a friendly sign-off.                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |

---

### Running it

```bash
python calculator.py
```

You’ll see something like:

```
 _____________________
|  _________________  |
| |               0 | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
...
```

Just enter numbers and pick operations; the script takes care of the rest.

> **Tip:** Because of Python’s default division behavior, dividing by zero will raise a `ZeroDivisionError`. Feel free to add your own error-handling if you need it.

---

### Extending it

* **More operations** – drop additional functions (e.g., `power`, `sqrt`) in the function list and map them in `operations`.
* **Input validation** – wrap numeric inputs with `try/except` to catch bad entries.
* **CLI flags** – replace `input()` calls with `argparse` if you’d rather pass numbers and operators as command-line arguments.

---

Happy calculating! 🎉
