class Cashier:
    def __init__(self):
        pass

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
        if coins >= cost:
            return True
        else:
            return False