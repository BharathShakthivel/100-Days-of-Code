# TODO-1: Ask the user for input
import art
print(art.logo)
# TODO-2: Save data into dictionary {name: price}
z = "y"
out_dict ={}
while z.lower() == "y":
    x = input("What is your name: ")
    y = input("What is the Bid Price in $: ")
    out_dict[x] = y
# TODO-3: Whether if new bids need to be added
    z = input("Do you have other biders? Y/N ")
    if z == "y":
        print("\n" * 20)
temp = 0
for i in out_dict:
    if int(out_dict[i]) > int(temp):
        temp = out_dict[i]

# TODO-4: Compare bids in dictionary
def get_key_by_value(out_dict, temp):
    for key, val in out_dict.items():
        if val == temp:
            print(f"The winner is {key} with a bid of ${val}")
    return None  # If value is not found
get_key_by_value(out_dict,temp)
