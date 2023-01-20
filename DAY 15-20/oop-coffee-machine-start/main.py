from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

end_of_program = False

while not end_of_program:
    order = input(f"What would you like ({menu.get_items()}): ").lower()
    if order == "report":
        coffee_maker.report()
        money_machine.report()
    elif order == "off":
        end_of_program = True
    else:
        drink = menu.find_drink(order)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)













