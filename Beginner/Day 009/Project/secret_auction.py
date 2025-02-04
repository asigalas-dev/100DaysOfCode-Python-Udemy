import os

def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")

from art import logo
print(logo)

def find_winner(bids_dictionary):
    highest_bid = 0
    winner = ""
    for bidder in bids_dictionary:
        bid_amount = bids_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}.")
run = True

bids = {}

while run:
    if run:
        name = input("What is your name?: ")
        bid = float(input("What is your bid? $"))
        bids[name] = bid
        choice = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
        clear_terminal()
        if choice == "no":
            run = False
            clear_terminal()

find_winner(bids)

