import random

"""Randomly pick customer and print customer info"""
    #import random command above is given defined functions to pick winner
from customers import get_customers_from_file

        #function to call above definded with customers as arguement.
def pick_winner(customers):
    """Choose random winner from customer file after import."""
    #call to randomly choose customer in customer file.
    chosen_customer = random.choice(customers)
    #announcement to print the winner and contact information to 
    #notify them they won
    print "Tell {name} at {email} that they've won".format(
        name=chosen_customer.name,
        email=chosen_customer.email
        )

    #runs the program to pick customers from our customer file.
def run_raffle():
    """Run the weekly raffle."""
        #setting variable to call the function and return weekly winner.
    customers = get_customers_from_file("customers.txt")
    pick_winner(customers)


if __name__ == "__main__":
    run_raffle()
