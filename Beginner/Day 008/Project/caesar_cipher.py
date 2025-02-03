from art import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(direction_choice, original_text, shift_amount):
    ciphered_text = ""
    if direction_choice == "decode":
        shift_amount *= -1
    for char in original_text:
        if char in alphabet:
            index_position = alphabet.index(char) + shift_amount
            index_position %= len(alphabet)
            ciphered_text += alphabet[index_position]
        else:
            ciphered_text += char
    print(f"Here is the {direction_choice}d result: {ciphered_text}")

restart = True
while restart:
    while True:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        if direction in ["encode", "decode"]:
            break
        print("You have typed the wrong command.")
    text = input("Type your message:\n").lower()
    while True:
        shift = input("Type the shift number:\n")
        if shift.isdigit():
            shift = int(shift)
            break
        print("Wrong input. Please, choose a whole number (no decimals).")

    caesar(direction, text, shift)

    while True:
        choice = str(input('''Would you like to restart the cipher program?
Type 'yes' if you want to go again. Otherwise, type 'no'\n''')).lower()
        if choice in ["yes", "no"]:
            break
        print("Invalid input. Please type 'yes' or 'no'.")

    if choice == "no":
        restart = False
        print("Goodbye!")
