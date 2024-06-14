### Data ###

recipes = {
    "small": {
        "ingredients": {
            "bread": 2,  ## slice
            "ham": 4,  ## slice
            "cheese": 4,  ## ounces
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,  ## slice
            "ham": 6,  ## slice
            "cheese": 8,  ## ounces
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,  ## slice
            "ham": 8,  ## slice
            "cheese": 12,  ## ounces
        },
        "cost": 5.5,
    }
}

resources = {
    "bread": 12,  ## slice
    "ham": 18,  ## slice
    "cheese": 24,  ## ounces
}


### Complete functions ###

class SandwichMachine:

    def __init__(self, machine_resources):
        """Receives resources as input.
           Hint: bind input variable to self variable"""
        self.machine_resources = machine_resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        if self.machine_resources["bread"] < ingredients["bread"]:
            print("Sorry there is not enough bread.")
            return False
        elif self.machine_resources["ham"] < ingredients["ham"]:
            print("Sorry there is not enough ham.")
            return False
        elif self.machine_resources["cheese"] < ingredients["cheese"]:
            print("Sorry there is not enough cheese.")
            return False
        return True

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        print("Please insert coins.")
        num_dollars = int(input("How many dollars are you inserting? "))
        num_half_dollars = int(input("How many half dollars are you inserting? "))
        num_quarters = int(input("How many quarters are you inserting? "))
        num_nickles = int(input("How many nickles are you inserting? "))
        return num_dollars + num_half_dollars * .5 + num_quarters * .25 + num_nickles * .05

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        if coins >= cost :
            return True
        else:
            return False

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources.
           Hint: no output"""
        self.machine_resources["bread"] -= order_ingredients["bread"]
        self.machine_resources["ham"] -= order_ingredients["ham"]
        self.machine_resources["cheese"] -= order_ingredients["cheese"]
        print(sandwich_size + " sandwich is ready. Bon appetit!")

### Make an instance of SandwichMachine class and write the rest of the codes ###
subway = SandwichMachine(resources)
command = input("What would you like? (small/ medium/ large/ off/ report) ")
if command == "off":
    print("turning off")
elif command == "report":
    print("bread: " + str(subway.machine_resources["bread"]) + " slice(s)")
    print("ham: " + str(subway.machine_resources["ham"]) + " slice(s)")
    print("cheese: " + str(subway.machine_resources["cheese"]) + " slice(s)")
else:
    if subway.check_resources(recipes[command]["ingredients"]):
        payment = subway.process_coins()
        if subway.transaction_result(payment, recipes[command]["cost"]):
            if payment > recipes[command]["cost"]:
                print("Here is $" + str(round(payment - recipes[command]["cost"], 2)) + " in change")
            subway.make_sandwich(command, recipes[command]["ingredients"])
        else:
            print("Sorry, that’s not enough money. Money refunded.")

