## ☕ Coffee Machine Project

This Python-based Coffee Machine project simulates a simple beverage vending machine. The user can order different types of coffee (espresso, latte, cappuccino), and the machine checks resources, processes payment using coin inputs, and provides change and the drink accordingly.

---

### 🧾 Features

* Offers **Espresso**, **Latte**, and **Cappuccino**
* Checks for **sufficient resources** before preparing a drink
* Accepts **virtual coins** (quarters, dimes, nickels, pennies)
* Handles **transactions** and calculates change
* Maintains and displays a **running report** of resources and profit
* Supports a shutdown command (`off`)

---

### 🧠 Code Breakdown

#### 1. **Menu and Resources**

```python
MENU = { ... }
resources = { ... }
```

* `MENU` is a dictionary containing drink types, their required ingredients, and cost.
* `resources` tracks the current stock of water, milk, and coffee.

---

#### 2. **`sufficient_for_order(choice)` Function**

Checks if the ingredients are available in sufficient quantities:

```python
def sufficient_for_order(choice):
```

* If a required ingredient is not enough, it prints a message and returns `False`.
* Otherwise, it deducts the used ingredients from the `resources`.

---

#### 3. **`process_coins(choice, coins)` Function**

Processes the payment:

```python
def process_coins(choice, coins):
```

* Checks if the user has inserted enough money.
* If so, it updates the profit, calculates and returns the change.
* If not, it refunds the money.

---

#### 4. **Main Loop**

```python
while is_on:
```

* Accepts user input (`espresso`, `latte`, `cappuccino`, `report`, or `off`).
* `report`: Displays current resources and profit.
* `off`: Shuts down the machine.
* If a drink is selected:

  * Checks resource availability.
  * Prompts the user for coin input (`quarters dimes nickles pennies`).
  * Converts coin input to total dollar value.
  * Calls `process_coins()` to handle payment.
  * If successful, serves the drink.

---

### 🧪 Example Interaction

```
What would you like to order? (Espresso/latte/cappuccino) latte
Enter the coins and specify, how many quarters,dimes,nickles,pennies: 10 0 0 0
Here is the change: 0.0$
Here is your latte☕, Enjoy!
```

---

### 🧰 Future Improvements

* Add GUI using Tkinter or PyQt
* Save and load resource state from a file
* Add option to refill ingredients
