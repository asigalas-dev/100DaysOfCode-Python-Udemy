import art, random

print(art.logo)

print("Welcome to the Number Guessing Game!")

number_to_guess = random.randint(1, 100)
print("I'm thinking of a number between 1 and 100.")

print(f"Hey! I am actually thinking of {number_to_guess}.")

difficulty = input("Choose your difficulty. Type 'easy' or 'hard': ").lower()

if difficulty == "hard":
    attempts = 5
else:
    attempts = 10

while attempts != -1:
    if attempts == 0:
        print(f'''You 've run out of guesses.
The number you were looking for was {number_to_guess}. 
Refresh the page to run again.''')
        break
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess > number_to_guess:
        print("Too high.")
        attempts -= 1
    elif guess < number_to_guess:
        print("Too low.")
        attempts -= 1
    elif guess == number_to_guess:
        print(f"You got it! The answer was {number_to_guess}.")
        break