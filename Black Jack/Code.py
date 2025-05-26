#Importing required libraries
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def black_jack():
  game = True
  while game:
   import art
   print(art.logo)
   user = random.choices(cards, k=2)
   computer = random.choices(cards, k=2)
   user_score = sum(int(x) for x in user)
   computer_score = sum(int(x) for x in computer)
   if 11 in computer:
    if sum(int(x) for x in computer) == 21:
      print("Computer got Blackjack")
      print("You Lose")
      game = False
   elif 11 in user:
    if sum(int(x) for x in user) == 21 and sum(int(x) for x in computer) != 21:
      print("You got Blackjack")
      print("You win")
      game = False
   if 11 in computer and computer_score > 21:
     computer_score-= 10
   elif 11 in user and user_score > 21:
     user_score-= 10
   print(f"Your Cards: {user}, current score: {user_score}")
   print(f"Computer's first card: {computer[0]}")
   keep_going = True
   while keep_going:
    another_card = input("Type 'y' to get another card, type 'n' to pass: ")
    if another_card.lower() == 'y':

      user.append(random.choice(cards))
      computer.append(random.choice(cards))
      user_score = sum(int(x) for x in user)
      computer_score = sum(int(y) for y in computer)
      if 11 in computer and computer_score > 21:
        computer_score -= 10
        print(f"Your Cards: {user}, current score: {user_score}")
        print(f"Computer's first card: {computer[0]}")
        if user_score > 21:
         print(f"Your final hand: {user}, final score: {user_score}")
         print(f"Computer final hand: {computer}, Computer final score: {computer_score}")
         print("You went over, You Lose")
         keep_going = False

      elif 11 in user and user_score > 21:
        user_score -= 10
        print(f"Your Cards: {user}, current score: {user_score}")
        print(f"Computer's first card: {computer[0]}")
        if user_score > 21:
         print(f"Your final hand: {user}, final score: {user_score}")
         print(f"Computer final hand: {computer}, Computer final score: {computer_score}")
         print("You went over, You Lose")
         keep_going = False
      elif user_score > 21:
       print(f"Your final hand: {user}, final score: {user_score}")
       print(f"Computer final hand: {computer}, Computer final score: {computer_score}")
       print("You went over, You Lose")
       keep_going = False

      elif computer_score > 21:
       print(f"Your final hand: {user}, final score: {user_score}")
       print(f"Computer final hand: {computer}, Computer final score: {computer_score}")
       print("Computer went over, You Won")
       keep_going = False

    elif another_card.lower() == 'n':
     while computer_score < 16:
      computer.append(random.choice(cards))
      computer_score = sum(int(y) for y in computer)
     if sum(int(x) for x in user) > computer_score:
      print(f"Your Cards: {user}, final score: {sum(int(x) for x in user)}")
      print(f"Computer final hand: {computer}, Computer final score: {computer_score}")
      print("You Won")
      keep_going = False
     elif sum(int(x) for x in user) < computer_score:
      print(f"Your Cards: {user}, final score: {sum(int(x) for x in user)}")
      print(f"Computer final hand: {computer}, Computer final score: {computer_score}")
      print("You Lost")
      keep_going = False
     elif sum(int(x) for x in user) == computer_score:
      print(f"Your Cards: {user}, final score: {sum(int(x) for x in user)}")
      print(f"Computer final hand: {computer}, Computer final score: {computer_score}")
      print("It's a draw")
      keep_going = False
   game = False

end_game = True
while end_game:
 option = input("Do you want to play the Black Jack game 'y' or 'n'? ")
 if option.lower() == "y":
  black_jack()
 else:
  print("Game Over")
  end_game = False

