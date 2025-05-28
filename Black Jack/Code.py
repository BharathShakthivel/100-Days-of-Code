# --------------------- OWN CODE ------------------------


#Importing required libraries
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def calculate_score(hand):
    score = sum(hand)
    while score > 21 and 11 in hand:
        hand[hand.index(11)] = 1
        score = sum(hand)
    return score

def black_jack():
  game = True
  while game:
   import art
   print(art.logo)
   user = random.choices(cards, k=2)
   computer = random.choices(cards, k=2)
   user_score = calculate_score(user)
   computer_score = calculate_score(computer)
   if 11 in computer:
    if computer_score == 21:
      print("Computer got Blackjack")
      print("You Lose")
      game = False
   elif 11 in user:
    if user_score == 21 and computer_score != 21:
      print("You got Blackjack")
      print("You win")
      game = False
   if 11 in computer and computer_score > 21:
       for i in range(len(computer)):
           if computer[computer.index(i)] == 11:
               computer.remove(11)
               computer.append(1)
   elif 11 in user and user_score > 21:
       for i in range(len(user)):
           if user[user.index(i)] == 11:
               user.remove(11)
               user.append(1)
   print(f"Your Cards: {user}, current score: {user_score}")
   print(f"Computer's first card: {computer[0]}")
   keep_going = True
   while keep_going:
    another_card = input("Type 'y' to get another card, type 'n' to pass: ")
    if another_card.lower() == 'y':

      user.append(random.choice(cards))
      computer.append(random.choice(cards))
      user_score = calculate_score(user)
      computer_score = calculate_score(computer)
      print(f"Your Cards: {user}, current score: {user_score}")
      print(f"Computer's first card: {computer[0]}")
      if 11 in computer and computer_score > 21:
        for i in range(len(computer)):
            if computer[computer.index(i)] == 11:
                computer.remove(11)
                computer.append(1)
        computer_score = calculate_score(computer)
        if user_score > 21:
         print(f"Your final hand: {user}, final score: {user_score}")
         print(f"Computer final hand: {computer}, Computer final score: {computer_score}")
         print("You went over, You Lose")
         keep_going = False

      elif 11 in user and user_score > 21:
        for i in range(len(user)):
            if user[user.index(i)] == 11:
                user.remove(11)
                user.append(1)
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
      computer_score = calculate_score(computer)
     if sum(int(x) for x in user) > computer_score:
      print(f"Your Cards: {user}, final score: {calculate_score(user)}")
      print(f"Computer final hand: {computer}, Computer final score: {computer_score}")
      print("You Won")
      keep_going = False
     elif sum(int(x) for x in user) < computer_score:
      print(f"Your Cards: {user}, final score: {calculate_score(user)}")
      print(f"Computer final hand: {computer}, Computer final score: {computer_score}")
      print("You Lost")
      keep_going = False
     elif sum(int(x) for x in user) == computer_score:
      print(f"Your Cards: {user}, final score: {calculate_score(user)}")
      print(f"Computer final hand: {computer}, Computer final score: {computer_score}")
      print("It's a draw")
      keep_going = False
   game = False


end_game = True
while end_game:
 option = input("Do you want to play the Black Jack game 'y' or 'n'? ")
 if option.lower() == "y":
  print("\n" * 20)
  black_jack()
 else:

  print("Game Over")
  end_game = False






# --------------------- FINALIZED STANDARD CODE ------------------------

import random
import art

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def calculate_score(hand):
    score = sum(hand)
    while score > 21 and 11 in hand:
        hand[hand.index(11)] = 1
        score = sum(hand)
    return score


def black_jack():
    print(art.logo)
    user = random.choices(cards, k=2)
    computer = random.choices(cards, k=2)
    user_score = calculate_score(user)
    computer_score = calculate_score(computer)

    # Check for blackjack
    if user_score == 21:
        print("You got Blackjack! You win 🥳")
        return
    elif computer_score == 21:
        print("Computer got Blackjack! You lose 😞")
        return

    print(f"Your cards: {user}, current score: {user_score}")
    print(f"Computer's first card: {computer[0]}")

    # Player decision loop
    while user_score < 21:
        if input("Type 'y' to get another card, 'n' to pass: ").lower() == 'y':
            user.append(random.choice(cards))
            user_score = calculate_score(user)
            print(f"Your cards: {user}, current score: {user_score}")
        else:
            break

    # Computer draws
    while computer_score < 16:
        computer.append(random.choice(cards))
        computer_score = calculate_score(computer)

    # Final comparison
    print(f"\nYour final hand: {user}, final score: {user_score}")
    print(f"Computer's final hand: {computer}, final score: {computer_score}")
    if user_score > 21:
        print("You went over. You lose 😭")
    elif computer_score > 21 or user_score > computer_score:
        print("You win 😎")
    elif user_score < computer_score:
        print("You lose 😤")
    else:
        print("It's a draw 🙃")


# Game loop
while input("Do you want to play Blackjack? Type 'y' or 'n': ").lower() == 'y':
    print("\n" * 10)
    black_jack()
print("Thanks for playing! 👋")





# --------------------- FINAL GUIDED CODE ------------------------



import random
from art import logo


def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(u_score, c_score):
    """Compares the user score u_score against the computer score c_score."""
    if u_score == c_score:
        return "Draw 🙃"
    elif c_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif u_score == 0:
        return "Win with a Blackjack 😎"
    elif u_score > 21:
        return "You went over. You lose 😭"
    elif c_score > 21:
        return "Opponent went over. You win 😁"
    elif u_score > c_score:
        return "You win 😃"
    else:
        return "You lose 😤"


def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    print("\n" * 20)
    play_game()









