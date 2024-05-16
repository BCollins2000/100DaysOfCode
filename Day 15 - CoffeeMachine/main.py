# Given Code: The Menu Defines the types of Coffee Drinks available, and their costs (both in ingredients used and money).
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk" : 0,
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

resources = {
    "water": 249,
    "milk": 1000,
    "coffee": 1000,
}

# Define a function called drink_resources: Identifies whether there are sufficient resources to produce the drink that is chosen as an input parameter. Insufficient resources are printed to the user.
def drink_resources(drink):
    if drink in MENU:
        depleted_resources = []
        for res in resources:
            if resources[res] - MENU[drink]["ingredients"][res] < 0:
                depleted_resources.append(res)
        if len(depleted_resources) == 0:
            return 'yes'
        else:
            print(f"Sorry we don't have enough {', '.join(depleted_resources)} to make a {drink}")
            return 'no'
    else:
        print(f"{drink} is not on the menu.")

# Define a function called drink_resources: Identifies whether there are sufficient resources to produce the drink that is chosen as an input parameter. Insufficient resources are printed to the user.
def deduct_resources(drink):
    if drink in MENU:
        for res in resources:
            resources[res] = resources[res] - MENU[drink]["ingredients"][res]
    else:
        print(f"{drink} is not on the menu.")
def drink_payment(drink):
    if drink in MENU:
        print(f"{drink} costs {MENU[drink]['cost']}")
        quarters = int(input("How many quarters? "))
        dimes = int(input("How many dimes? "))
        nickels = int(input("How many nickels? "))
        pennies = int(input("How many pennies? "))
        amount_paid = round(0.25*quarters + 0.1*dimes + 0.05*nickels + 0.01*pennies, 2)
        if amount_paid >= round(float(MENU[drink]['cost']), 2):
            print(f"You paid {amount_paid} and  {drink} costs {MENU[drink]['cost']}. Your change is {round(amount_paid - round(float(MENU[drink]['cost']), 2), 2)}")
            print(f"Enjoy your {drink}!")
            return 'yes'
        else:
            print(f"You paid {amount_paid} and  {drink} costs {MENU[drink]['cost']}. You did not pay enough")
            return 'no'
    else:
        print(f"{drink} is not on the menu.")




#1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
#2. Turn off the Coffee Machine by entering “off” to the prompt.

def coffee():
    new_selection = 'yes'
    while new_selection == 'yes':
        selection = input("What would you like? (espresso/latte/cappuccino)")
        if selection == 'off':
            return print("Coffee Machine Turning Off...")
        elif selection == 'report':
            for res in resources:
                print(f'We have {resources[res]} {res} remaining')
            new_selection = input("Make a drink selection? 'yes' or 'no'")
        elif selection in MENU:
            if drink_resources(selection) == 'yes':
                if drink_payment(selection) == 'yes':
                    deduct_resources(selection)
                    new_selection = input("Make a drink selection? 'yes' or 'no'")
                else:
                    new_selection = input("Make a drink selection? 'yes' or 'no'")
        else:
            return print("Sorry, you made an invalid selection. Goodbye!")
    print("Goodbye!")

coffee()


