import art, random

EASY_ATTEMPTS = 10
HARD_ATTEMPTS = 5

def choose_difficulty():
    difficulty = input("Choose your difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == "hard":
        return HARD_ATTEMPTS
    else:
        return EASY_ATTEMPTS

def check_answer(u_guess, num_guess, attempts):
    if u_guess > num_guess:
        print("Too high.")
        return attempts - 1
    elif u_guess < num_guess:
        print("Too low.")
        return attempts - 1
    elif u_guess == num_guess:
        print(f"You got it! The answer was {num_guess}.")

def game():
    print(art.logo)

    print("Welcome to the Number Guessing Game!")

    number_to_guess = random.randint(1, 100)
    print("I'm thinking of a number between 1 and 100.")
    print(f"Hey! I am actually thinking of {number_to_guess}.")

    attempts = choose_difficulty()

    guess = 0
    while guess != number_to_guess:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        attempts = check_answer(guess,number_to_guess, attempts)
        if attempts == 0:
            print(f'''You 've run out of guesses.
The number you were looking for was {number_to_guess}. 
Refresh the page to run again.''')
            return
        else:
            print("Guess again.")
game()