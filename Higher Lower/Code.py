import art, random, game_data
print(art.logo)
score = 0
current_A = random.choice(game_data.data)
game_data.data.remove(current_A)
print(f"Compare A: {current_A['name']},a {current_A['description']},from {current_A['country']}")
print(art.vs)
current_B = random.choice(game_data.data)
game_data.data.remove(current_B)
print(f"Against B: {current_B['name']},a {current_B['description']},from {current_B['country']}")
while score != 50 :
    user_choice = input("Who has more Followers. Type 'A' or 'B': ")
    if user_choice.lower() == 'a' and current_A['follower_count'] > current_B['follower_count']:
        score+=1
        print(f"You're Right! Current Score: {score}")
        print(f"Compare A: {current_A['name']},a {current_A['description']},from {current_A['country']}")
        print(art.vs)
        current_B = random.choice(game_data.data)
        game_data.data.remove(current_B)
        print(f"Against B: {current_B['name']},a {current_B['description']},from {current_B['country']}")

    elif user_choice.lower() == 'b' and current_B['follower_count'] > current_A['follower_count']:
        score+=1
        print(f"You're Right! Current Score: {score}")
        current_A = current_B
        print(f"Compare A: {current_A['name']},a {current_A['description']},from {current_A['country']}")
        print(art.vs)
        current_B = random.choice(game_data.data)
        game_data.data.remove(current_B)
        print(f"Against B: {current_B['name']},a {current_B['description']},from {current_B['country']}")
    elif len(game_data.data) == 0:
        print("You have won the game. Congrats!")
        break
    else:
        print(f"Sorry, That's Wrong. Final Score: {score}")
        break

