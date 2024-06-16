import data
from sandwich_maker import SandwichMaker
from cashier import Cashier

# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()

def main():
    ###  write the rest of the codes ###
    while True:
        command = input("What would you like? (small/ medium/ large/ off/ report) ")
        if command == "off":
            print("turning off")
            break
        elif command == "report":
            print("bread: " + str(resources["bread"]) + " slice(s)")
            print("ham: " + str(resources["ham"]) + " slice(s)")
            print("cheese: " + str(resources["cheese"]) + " slice(s)")
        else:
            if sandwich_maker_instance.check_resources(recipes[command]["ingredients"]):
                payment = cashier_instance.process_coins()
                if cashier_instance.transaction_result(payment, recipes[command]["cost"]):
                    if payment > recipes[command]["cost"]:
                        print("Here is $" + str(round(payment - recipes[command]["cost"], 2)) + " in change")
                    sandwich_maker_instance.make_sandwich(command, recipes[command]["ingredients"])
                else:
                    print("Sorry, that’s not enough money. Money refunded.")

if __name__=="__main__":
    main()
