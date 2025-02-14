MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

original_resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0

def can_make_drink(order_ingredients):
    """Checks if there are enough resources to make the given drink."""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry. Not enough {item}")
            return False
    return True

def print_report():
    print(f'''Water: {resources["water"]}ml
Milk: {resources["milk"]}ml
Coffee: {resources["coffee"]}g
Money: ${format(money, ".2f")}''')

def update_resources(order_ingredients):
    """Deducts resources needed for making a coffee from the total resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]

def restock(resources_dict, og_resources):
    """Restocks resources"""
    resources_dict.clear()
    resources_dict.update(og_resources)

on = True

while on:
    drink_choice = input("What would you like to drink? (espresso/latte/cappuccino): ")
    if drink_choice == "report":
        print_report()
    elif drink_choice == "restock":
        restock(resources, original_resources)
    elif drink_choice == "off":
        on = False
    elif drink_choice not in MENU:
        print("❌ You haven't typed your choice correctly. Please, try again.")
    elif can_make_drink(MENU[drink_choice]["ingredients"]):
        print("Please insert coins.")
        quarters = int(input("How many quarters? : ")) * 0.25
        dimes = int(input("How many dimes? : ")) * 0.10
        nickels = int(input("How many nickels? : ")) * 0.05
        pennies = int(input("How many pennies? : ")) * 0.01
        total_coins = quarters + dimes + nickels + pennies
        if MENU[drink_choice]["cost"] < total_coins:
            money += MENU[drink_choice]["cost"]
            update_resources(MENU[drink_choice]["ingredients"])
            change = format(total_coins - MENU[drink_choice]["cost"], ".2f")
            print(f"Here is ${change} dollars in change.")
            print(f"Here is your {drink_choice} ☕. Enjoy!")
        else:
            print("Sorry that's not enough money. Money refunded.")
