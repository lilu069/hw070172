def main():
    print("This program calculates the cost of an order at Konditorei coffee shop.")
    print()
    print("Please enter the amount of coffee you want to purchase")
    pounds = eval (input("pounds of coffee: "))
    cost = (pounds * 10.50) + (pounds * 0.86) + 1.50

    print("The costs for the order incl. shipping are",  cost, "pounds.")
main()
