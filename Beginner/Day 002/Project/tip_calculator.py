print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

total = (bill+(tip / 100 * bill)) # total amount of bill including the tip
split_amount = round((total / people), 2) # amount of money each will pay

print(f"Each person should pay: ${split_amount:.2f}") # :.2f gives us 2 decimal points, :.1f would give 1 decimal point

# Another way to do it would be
# split_amount= "{:.2f}".format(total / people)
# print(f"Each person should pay: ${split_amount}")