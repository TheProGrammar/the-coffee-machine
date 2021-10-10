from data import MENU
from data import resources as res


class CoffeeMachine:

    def run(self):
        answer = self._user_prompt().lower()
        processed_answer = self._process_user_answer(answer)

        if processed_answer == "drink":
            if self._has_enough_resources(answer):
                self._ask_for_payment(answer)


            else:
                print("Not enough resources.")
                print("The maintenance team has been informed the problem. We are sorry about this.")
        else:
            print("go to action")

    def _ask_for_payment(self, drink_type):
        print(f"The {drink_type} price is {MENU[drink_type]['cost']}")
        quarters = input("How many quarters you are paying with? ")


    def _process_coins(self):
        pass

    @staticmethod
    def _process_user_answer(user_answer):
        if user_answer in ["espresso", "latte", "cappuccino"]:
            return "drink"
        else:
            return "action"

    def _user_prompt(self):
        self.user_choice = input("What would you like to order? Espresso, latte or cappuccino? ")
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
                return False
        else:
            if res["water"] > ingredients["water"] and res["milk"] > ingredients["milk"] and res["coffee"] > ingredients["coffee"]:
                return True
            else:
                return False


coffee = CoffeeMachine()
coffee.run()
