from data import MENU
from data import resources as res


class CoffeeMachine:
    def __init__(self):
        self.user_choice = input("What would you like to order? Espresso, latte or cappuccino? ")

    def run(self):
        # Ask a user for the drink name and store it
        answer = self._user_prompt().lower()
        # Check if the machine has enough resources for the wanted drink (return True)
        if self._has_enough_resources(answer):
            print("enough resources")

    def _user_prompt(self):
        while self.user_choice.lower() not in ["espresso", "latte", "cappuccino", "report", "off"]:
            print("Invalid answer. Please type the drink name exactly as is.")
            self.user_choice = input("What would you like to order? Espresso, latte or cappuccino? ")
        return self.user_choice

    @staticmethod
    def _has_enough_resources(wanted_drink):
        ingredients = MENU[wanted_drink]["ingredients"]
        if wanted_drink == "espresso":
            if res["water"] > ingredients["water"] and res["coffee"] > ingredients["coffee"]:
                return True
        else:
            if res["water"] > ingredients["water"] and res["milk"] > ingredients["milk"] and res["coffee"] > ingredients["coffee"]:
                return True


coffee = CoffeeMachine()
coffee.run()
