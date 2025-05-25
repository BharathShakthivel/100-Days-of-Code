#Importing required libraries
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
option = input("Do you want to play the Black Jack game 'y' or 'n'? ")

if option.lower() == "y":
 game = True
 while game:
  import art
  print(art.logo)
  user = random.choices(cards, k=2)
  computer = random.choices(cards, k=2)
  print(f"Your Cards: {user}, current score: {sum(int(x) for x in user)}")
  print(f"Computer's first card: {computer[0]}")
  if 11 in user:
   if sum(int(x) for x in user) > 23:
    
  another_card = input("Type 'y' to get another card, type 'n' to pass: ")
  if another_card.lower() == 'y':
   user.append(random.choice(cards))
   computer.append(random.choice(cards))
   print(f"Your Cards: {user}, current score: {sum(int(x) for x in user)}")
   print(f"Computer's first card: {computer[0]}")
   game = False
  # else:
  #  game = False
