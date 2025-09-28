Higher or Lower Game (Followers Edition)

This is a simple Python terminal game inspired by the classic "Higher or Lower" format. The game compares the number of followers of different celebrities, brands, and public figures, and the player must guess who has more followers.


---

🎮 How the Game Works

1. At the start of the game, a random entry from the game_data dataset is chosen as Option A.


2. Another random entry is chosen as Option B.


3. The player is shown both options with their name, description, and country of origin—but not their follower counts.


4. The player must guess who has more followers by typing:

A → if they think Option A has more followers

B → if they think Option B has more followers



5. If the player guesses correctly:

Their score increases by 1

The correct choice becomes the new Option A

A new random entry is chosen as Option B



6. If the player guesses incorrectly:

The game ends and their final score is displayed.



7. If the dataset runs out of options before the player loses:

The game ends with a congratulatory message.





---

📂 Project Structure

art.py → Contains ASCII art like the game logo and the "VS" symbol used for display.

game_data.py → Contains a list of dictionaries. Each dictionary represents a person/brand with the following keys:

name → Name of the person/brand

follower_count → Number of followers (hidden from the player)

description → What they are known for

country → Their country of origin


main.py → The main game logic (the code shown above).



---

🛠️ Features

Randomized gameplay using Python’s random module.

Score tracking system.

Dynamic comparisons where winners carry over as the next Option A.

Game ends either on a wrong guess or when the dataset is exhausted.



---

🚀 How to Run

1. Clone the repository:

git clone https://github.com/yourusername/higher-lower-game.git
cd higher-lower-game


2. Run the Python script:

python main.py




---

✅ Example Gameplay

Compare A: Cristiano Ronaldo, a Footballer, from Portugal
vs
Against B: Ariana Grande, a Musician, from USA
Who has more Followers. Type 'A' or 'B':

If the player types A or B, the program checks and updates the score accordingly.


---

📌 Future Improvements

Add more entries to game_data.py for variety.

Add replay functionality after game over.

Allow difficulty levels (e.g., only pick from close follower counts).

Add colorized terminal output for a better experience.
