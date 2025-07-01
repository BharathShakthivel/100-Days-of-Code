import art, random, game_data
print(art.logo)
while len(game_data.data) > 0 :
    random_A_num = random.randrange(1,len(game_data.data))
    current_A = game_data.data.pop(random_A_num)
    print(f"Compare A: {current_A['name']},a {current_A['description']},from{current_A['country']}")
    print(art.vs)
    random_B_num = random.randrange(1, len(game_data.data))
    current_B = game_data.data.pop(random_B_num)
    print(f"Against B: {current_B['name']},a {current_B['description']},from{current_B['country']}")
    print("Who has more Followers. Type 'A' or 'B': ")
