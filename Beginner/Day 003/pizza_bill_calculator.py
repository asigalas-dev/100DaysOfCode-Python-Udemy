print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
bill = 0

# Price calculation for size
# Added the .lower() to account for a capital or lower case letter
if size.lower() == "s":
    bill += 15
elif size.lower() == "m":
    bill += 20
elif size.lower() == "l":
    bill += 25
else:
    print("You typed the wrong input.")

# Price calculation for Pepperoni
if pepperoni.lower() == "y":
    if size.lower() == "s":
        bill += 2
    else:
        bill +=3
elif pepperoni.lower() != "n":
    print("You typed the wrong input.")

# Price calculation for Extra Cheese
if extra_cheese.lower() == "y":
    bill += 1
elif extra_cheese.lower() != "n":
    print("You typed the wrong input.")

# Print total bill
print(f"Your final bill is: ${bill}.")
