import art
print(art.logo)

print("Welcome to Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

difficulty = input("Choose a difficulty. Typer 'easy' or 'hard': ")
life = 0
if difficulty.lower() == "easy":
    life = 10
else:
    life = 5
print(f"You have {life} attempts remaining to guess the number")
guess = input("Make a Guess: ")
