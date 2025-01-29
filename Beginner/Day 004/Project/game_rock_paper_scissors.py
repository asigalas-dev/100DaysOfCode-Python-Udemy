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

# Ask user for a choice of rock, paper or scissors
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if user_choice <0 or user_choice >2:
    print("Invalid input. You lose.")
else:
    # Assigned ascii art to a list
    choices = [rock, paper, scissors]
    print(f"You chose: \n{choices[user_choice]}")

    # Choosing a random number for computer
    comp_choice = random.randint(0, 2)
    print(f"Computer chose: \n{choices[comp_choice]}")

    if user_choice == comp_choice:
        print("It's a tie.")
    elif (user_choice == 0 and comp_choice == 2) or \
         (user_choice == 1 and comp_choice == 0) or \
         (user_choice == 2 and comp_choice == 1):
        print("You win!")
    else:
        print("You lose.")
