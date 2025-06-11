## 🛎️ Silent-Auction CLI Script — Code Walk-through

This script lets you run a quick “silent auction” from the command line.
Participants enter their names and bids, and when everyone is done the program announces the highest bidder.

```python
import art
print(art.logo)

# 1️⃣  Gather bids
z = "y"
out_dict = {}
while z.lower() == "y":
    x = input("What is your name: ")
    y = input("What is the Bid Price in $: ")
    out_dict[x] = y

    # 2️⃣  Check if more bidders will enter
    z = input("Do you have other biders? Y/N ")
    if z.lower() == "y":
        print("\n" * 20)      # simple “screen-clear” so bids stay secret

# 3️⃣  Find the highest bid
temp = 0
for i in out_dict:
    if int(out_dict[i]) > int(temp):
        temp = out_dict[i]

# 4️⃣  Announce the winner
def get_key_by_value(out_dict, temp):
    for key, val in out_dict.items():
        if val == temp:
            print(f"The winner is {key} with a bid of ${val}")
get_key_by_value(out_dict, temp)
```

### How the script works

| Stage                    | Purpose                                                                                                                                             | Key details |
| ------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| **Display banner**       | `art.logo` shows a stylised ASCII logo so users know they’re in the auction program.                                                                |             |
| **Gather bids**          | `while z.lower() == "y":` keeps looping as long as another bidder says **Y**. Each name/bid pair is stored in `out_dict` (`{"Alice": "150", ...}`). |             |
| **Hide previous bids**   | Printing 20 blank lines is a quick-and-dirty way to push earlier answers off screen so the next bidder can’t peek.                                  |             |
| **Identify the top bid** | Loop through the dictionary, cast each bid to `int`, and keep the largest value in `temp`.                                                          |             |
| **Reveal the winner**    | A helper function searches for the bidder whose value matches `temp` and prints the result.                                                         |             |

### Things to note / possible improvements

* **Convert bids to integers immediately:** store `out_dict[x] = int(y)` so you never need `int()` casting later.
* **Screen clearing:** `os.system("cls" if os.name == "nt" else "clear")` is more robust than printing blank lines.
* **Input validation:** reject non-numeric bids or negative numbers with `try/except` on `int()`.
* **Handling ties:** right now, if two people bid the same amount, only the first match is printed. Decide whether to split the pot or print all winners.
* **Exit option:** allow users to type **N** (case-insensitive) any time instead of looping until `Y` becomes something else.

