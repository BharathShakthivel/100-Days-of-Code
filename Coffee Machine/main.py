# Coffee Machine Project
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 4000,
    "milk": 20000,
    "coffee": 10000,
}
def sufficient_for_order(choice):
    if choice not in MENU:
        print("Invalid Entry")
        return False
    for i in MENU[choice]["ingredients"]:
        if (MENU[choice]["ingredients"][i]) <= resources[i]:
            resources [i] -= MENU[choice]["ingredients"][i]
        else:
            print(f"Sorry there is not enough {i}")
            print(f"Please refill {i}")
            return False
def process_coins(choice,coins):
    global profit, MENU
    if coins > MENU[choice]["cost"]:
        coins -= MENU[choice]["cost"]
        profit+= MENU[choice]["cost"]
        print(f"Here is the change: {round(coins,2)}$")
    else:
        print("Sorry that's not enough money. Money refunded")


profit = 0
# Main Execution begins here.
is_on = True
while is_on:
    choice = input("What would you like to order? (Espresso/latte/cappuccino) ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water:{resources["water"]} ml")
        print(f"Milk:{resources["milk"]} ml")
        print(f"Coffee:{resources["coffee"]} gm")
        print(f"Money:{profit} $")
    else:
     order_success = sufficient_for_order(choice)
     if order_success != False:
         values = input("Enter the coins and specify, how many quarters,dimes,nickles,pennies: ").split()
         quarters, dimes, nickles, pennies = map(float, values)
         coins = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
         current_order = process_coins(choice, coins)
         print(f"Here is your {choice}☕, Enjoy!")
     else:
         print("Try again")
         pass





