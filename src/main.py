from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Create objects
machine_menu = Menu()
resources_management = CoffeeMaker()
cash_machine = MoneyMachine()

while True:

    menu_choice = input(f"    What would you like? ({machine_menu.get_items()}): ")

    if menu_choice == "off":
        break
    elif menu_choice == "report":
        resources_management.report()
        cash_machine.report()
    else:
        drink_chosen = machine_menu.find_drink(menu_choice)

        if not drink_chosen:
            continue

        enough_resources = resources_management.is_resource_sufficient(drink_chosen)

        if not enough_resources:
            continue

        if not cash_machine.make_payment(drink_chosen.cost):
            continue

        resources_management.make_coffee(drink_chosen)
