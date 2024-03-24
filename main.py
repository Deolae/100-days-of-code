import coffee

action = ""


def report():
    # Prints a report of the current resources
    print(f"Water: {coffee.resources['water']}ml")
    print(f"Milk: {coffee.resources['milk']}ml")
    print(f"Coffee: {coffee.resources['coffee']}g")
    print(f"Money: ${coffee.resources['money']}")


def refill():
    coffee.resources['water'] = 300
    coffee.resources['milk'] = 200
    coffee.resources['coffee'] = 100


def check_resources():
    # Check if the resources to make the drink are enough, if not, print a message informing the user
    if coffee.MENU[action]['ingredients']['water'] > coffee.resources['water']:
        print("Sorry, there is not enough water.")
        return False
    elif coffee.MENU[action]['ingredients']['coffee'] > coffee.resources['coffee']:
        print("Sorry, there is not enough coffee.")
        return False
    # Espresso doesn't use milk, so only check for milk if it's the other 2 options
    elif action == "cappuccino" or action == "latte":
        if coffee.MENU[action]['ingredients']['milk'] > coffee.resources['milk']:
            print("Sorry, there is not enough milk.")
            return False
        else:
            return True
    else:
        return True


def process_coins():
    # Get coins from the user and check if it's enough to buy the requested drink
    print("Please insert coins.")
    quarters = 0.25 * int(input("How many quarters?: "))
    dimes = 0.10 * int(input("How many dimes?: "))
    nickles = 0.05 * int(input("How many nickles?: "))
    pennies = 0.01 * int(input("How many pennies?: "))
    # Calculate the total
    total = quarters + dimes + nickles + pennies
    # Calculate the change and round it to 2 decimal places
    change = round(total - coffee.MENU[action]['cost'], 2)

    if total > coffee.MENU[action]['cost']:
        print(f"Here is ${change} in change.")
        return True
    elif total == coffee.MENU[action]['cost']:
        return True
    else:
        print(f"Sorry that's not enough money, you put ${round(total,2)} in total, and {action} costs ${coffee.MENU[action]['cost']} ."
              f"Money refunded.")
        return False


def serve_customer():
    global action
    # Prompts the user to enter the action they wish to perform
    action = input('\nWhat would you like? (espresso [$1.5] / latte [$2.5] / cappuccino [$3.0] ), or type "other": ').lower()
    if action == "other":
        action = input('\nOther functions:- \n1.Type "report" for a resource report. \n2.Type "refill" for a resource '
                       'refill. \n3.Type "off" to shut down the coffee machine. \nAnswer: ')
        # Close the program if action is "off"
        if action == "off":
            exit()
        # Print a report if action is "report"
        elif action == "report":
            report()

        # Refill the resources if action is "refill"
        elif action == "refill":
            refill()

    # If there are enough resources and the coins processes successfully, give the user the drink
    elif check_resources() and process_coins():
        # First, deduct the resources used from the machine resources
        coffee.resources['water'] -= coffee.MENU[action]['ingredients']['water']
        coffee.resources['coffee'] -= coffee.MENU[action]['ingredients']['coffee']
        # Only deduct from milk if it's cappuccino or latte
        if action == "cappuccino" or action == "latte":
            coffee.resources['milk'] -= coffee.MENU[action]['ingredients']['milk']
        coffee.resources["money"] += coffee.MENU[action]['cost']

        # Second, give the user the drink
        print(f"Here is your {action} ☕. Enjoy!")

    # Prompt the user to enter a new action as long as the program is running
    serve_customer()


serve_customer()
