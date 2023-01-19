MENU = {
    "espresso": {"ingredients": {
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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def check_resource(order):
    """Check the availability of resources"""
    if order != "espresso":
        if resources["water"] < MENU[order]['ingredients']["water"]:
            return "Sorry, there is not enough water"
        elif resources["milk"] < MENU[order]['ingredients']["milk"]:
            return "Sorry, there is not enough milk"
        elif resources["coffee"] < MENU[order]['ingredients']["coffee"]:
            return "Sorry, there is not enough coffee"
    else:
        if resources["water"] < MENU[order]['ingredients']["water"]:
            return "Sorry, there is not enough water"
        elif resources["coffee"] < MENU[order]['ingredients']["coffee"]:
            return "Sorry, there is not enough coffee"


def report(order):
    """Give back the report about total amount of resources"""
    amount_spent = 0
    if order == "report":
        return f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g"
    elif order == "latte" or order == "cappuccino":
        resources["water"] = resources["water"] - MENU[order]["ingredients"]["water"]
        resources["milk"] = resources["milk"] - MENU[order]["ingredients"]["milk"]
        resources["coffee"] = resources["coffee"] - MENU[order]["ingredients"]["coffee"]
        amount_spent += MENU[order]["cost"]
        return f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g" \
               f"\nMoney: ${amount_spent}"
    else:
        resources["water"] = resources["water"] - MENU[order]["ingredients"]["water"]
        resources["coffee"] = resources["coffee"] - MENU[order]["ingredients"]["coffee"]
        amount_spent += MENU[order]["cost"]
        return f"Water: {resources['water']}ml\nCoffee: {resources['coffee']}g\nMoney: ${amount_spent}"


def coin_cost(order):
    """Count the total of change"""
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))

    totalcost = (quarters * 0.25) + (dimes * 0.1) + (nickles * 0.05) + (pennies * 0.01)
    totalback = round(totalcost - MENU[order]['cost'], 2)

    if totalcost >= MENU[order]['cost']:
        return f"Here is your ${totalback} in change."
    else:
        return "Sorry that's not enough money. Money refunded."


def coffee_program():
    """The main program of the coffee machine"""
    end_of_program = False
    while not end_of_program:
        order = input("What would you like?(espresso/latte/cappuccino): ").lower()
        if order == "report":
            print(report(order))
        elif order == "off":
            end_of_program = True
        elif check_resource(order):
            print(check_resource(order))
        else:
            print(report(order))
            print(coin_cost(order))
            print(f"Here is your {order} ☕ Enjoy!")


coffee_program()
