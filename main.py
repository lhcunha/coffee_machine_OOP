from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

should_continue = True

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

while should_continue:
    options = menu.get_items()
    user_input = input(f"What would you like? {options}: ")
    if user_input == "off":
        print("The machine is shutting down...")
        should_continue = False
    elif user_input == "report":        
        coffee_maker.report()
        money_machine.report()
    elif user_input not in menu.get_items():
        print("This is not a valid option!")
    else:
        drink = menu.find_drink(user_input)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
