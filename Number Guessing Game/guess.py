import art , random
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
random_num = random.randrange(1,101)
game = True
while game:
    guess = int(input("Make a Guess: "))
    if guess > random_num:
        print("Too High")
        print("Guess again")
        life -=1
        print(f"You have {life} attempts remaining to guess the number")
    elif guess < random_num:
        print("Too Low")
        print("Guess again")
        life -= 1
        print(f"You have {life} attempts remaining to guess the number")
    elif life == 0:
        print("You have run out guesses. Refresh the page to run again.")
        game = False
    elif guess == random_num:
        print("You got it")
        print(f"The answer was {random_num}")
        game = False


