from art import logo
import os

def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 == 0:
        return "Error! Division by zero is undefined."
    return n1 / n2

def get_number(prompt): #improve code in case user doesn't input number
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def format_number(n): # Formatting our numbers so that if they don't have decimals are presented as integers
    return int(n) if n.is_integer() else round(n, 2)

print(logo)

operations = {
    "+": add, # we are not using parenthesis with the functions because we are storing them. We are not using them
    "-": subtract,
    "*": multiply,
    "/": divide,
}

calculation = True

while calculation: # While it's True the calculator is running
    number_1 = get_number("What is your first number?: ")

    continue_with_number = True

    while continue_with_number: # While it's True we are continuing with the same number
        for o in operations:
            print(o)

        while True: # Checking for valid operation choice
            operation = input("Pick an operation: ")
            if operation in operations:
                break
            print("Invalid operation. Please choose a valid operator from the list.")

        number_2 = get_number("What is your second number? ")

        result = operations[operation](number_1, number_2)
        print(f"\n{format_number(number_1)} {operation} {format_number(number_2)} = {format_number(result)}")

        while True: # Checking for valid option input
            cont_calc = input(
                f"\nType 'y' to continue calculating with {format_number(result)}, "
                "'n' to start a new calculation, or 'end' to exit: "
            ).lower()

            if cont_calc in ["y", "n", "end"]:
                break  # Exit the loop if input is valid

            print("Invalid input. Please type 'y', 'n', or 'end'.")

        if cont_calc == "y":
            number_1 = result
        elif cont_calc == "n":
            continue_with_number = False
            clear_terminal()
        else:
            calculation = False
            continue_with_number = False

clear_terminal()
print("Thank you for using the calculator!")