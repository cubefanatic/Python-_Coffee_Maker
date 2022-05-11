from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def main_function():
    coffee_maker_off = False
    coffee_machine = CoffeeMaker()
    money_machine = MoneyMachine()
    menu_items = Menu()
    while coffee_maker_off is False:
        choice = input(f"what would you like {menu_items.get_items()}: ")
        if choice == "off":
            print("switching off..")
            coffee_maker_off = True
        elif choice == "report":
            coffee_machine.report()
            money_machine.report()
        elif choice == "espresso" or choice == "latte" or choice == "cappuccino":
            coffee_choice_item = menu_items.find_drink(choice)
            result = coffee_machine.is_resource_sufficient(coffee_choice_item)
            if result is True:
                is_successful = money_machine.make_payment(coffee_choice_item.cost)
                if is_successful is True:
                    coffee_machine.make_coffee(coffee_choice_item)


main_function()

