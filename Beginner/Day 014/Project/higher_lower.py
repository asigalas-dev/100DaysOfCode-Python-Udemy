import art, os
from game_data import data
from random import randint

# Clear Terminal
def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")

# Function to pick an article
def choose_article(letter):
    """It chooses an article 'a' or 'an' depending on the first letter of the description of each random choice."""
    vowels = ["a", "e", "i", "o", "u"]
    if letter.lower() in vowels:
        return "an"
    else:
        return "a"

# Function to check correct answer
def correct_answer(data_list, choice_a_num, choice_b_num):
    # Get follower count
    follower_count_a = data_list[choice_a_num]["follower_count"]
    follower_count_b = data_list[choice_b_num]["follower_count"]
    if follower_count_a > follower_count_b:
        return "a"
    else:
        return "b"

# Start game
game = True
score = 0

# Choosing a random number from the range of our data for A
choice_a = randint(0, len(data) - 1)

# Printing logo
print(art.logo)

while game:
    # Choosing a random number from the range of our data for B
    choice_b = randint(0, len(data) - 1)
    # Ensure a and b are not the same
    while choice_b == choice_a:
        choice_b = randint(0, len(data) - 1)

    # Assigning an article
    article_a = choose_article(data[choice_a]["description"][0])
    article_b = choose_article(data[choice_b]["description"][0])

    # Printing first choice
    print(f"Compare A: {data[choice_a]['name']}, {article_a} {data[choice_a]['description']}, from {data[choice_a]['country']}.")

    # Draw vs logo
    print(art.vs)

    # Printing second choice
    print(f"Against B: {data[choice_b]['name']}, {article_b} {data[choice_b]['description']}, from {data[choice_b]['country']}.")

    # Asking user to make a choice
    pick = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Clearing the terminal
    clear_terminal()

    # Check user choice against correct answer
    if pick == correct_answer(data, choice_a, choice_b):
        score += 1
        print(art.logo)
        print(f"You're right! Current score: {score}\n")
        choice_a = choice_b
    else:
        print(art.logo)
        print(f"Sorry, that's wrong. Final score: {score}.")
        break