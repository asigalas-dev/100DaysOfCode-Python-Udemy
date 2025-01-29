import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

lizard = '''
   _.--._       /|
 .'()..()`.    / /
( `-.__.-' )  ( ( 
 \   /\   /    \ \.
  \      /      ) )
.' -.__.- `.-.-'_.'
'''

spock = '''⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                      _    
 ___ _ __   ___   ___| | __
/ __| '_ \ / _ \ / __| |/ /
\__ \ |_) | (_) | (__|   < 
|___/ .__/ \___/ \___|_|\_\.           
    |_| 
'''

# Ask user for a choice of rock, paper or scissors
print('''Here are the rules of the game:
Rock: Crushes scissors and lizard, but loses to paper and Spock
Paper: Covers rock and disproves Spock, but loses to scissors and lizard
Scissors: Cuts paper and decapitates lizard, but loses to rock and Spock
Lizard: Eats paper and poisons Spock, but loses to scissors and rock
Spock: Vaporizes rock and smashes scissors, but loses to paper and lizard
''')
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors, 3 for Lizard or 4 for Spock.\n"))

if user_choice <0 or user_choice >4:
    print("Invalid input. You lose.")
else:
    # Assigned ascii art to a list
    choices = [rock, paper, scissors, lizard, spock]
    print(f"You chose: \n{choices[user_choice]}")

    # Choosing a random number for computer
    comp_choice = random.randint(0, 4)
    print(f"Computer chose: \n{choices[comp_choice]}")

    if user_choice == comp_choice:
        print("It's a tie.")
    elif (user_choice == 0 and (comp_choice == 2 or comp_choice == 3)) or \
         (user_choice == 1 and (comp_choice == 0 or comp_choice == 4)) or \
         (user_choice == 2 and (comp_choice == 1 or comp_choice == 3)) or \
         (user_choice == 3 and (comp_choice == 1 or comp_choice == 4)) or \
         (user_choice == 4 and (comp_choice == 0 or comp_choice == 2)):
        print("You win!")
    else:
        print("You lose.")
