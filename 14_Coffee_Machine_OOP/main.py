from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee = CoffeeMaker()
menu = Menu()
money = MoneyMachine()
turned_on = True

while turned_on == True:
    order = input(f"What would you like? ({menu.get_items()}): ")

    if order == "report":
        coffee.report()
        money.report()
    elif order == "off":
        exit()
    elif coffee.is_resource_sufficient(menu.find_drink(order)):
        if money.make_payment(menu.find_drink(order).cost):
            coffee.make_coffee(menu.find_drink(order))
