def main():
    print("This program calculates the cost per square inch of a circular pizza.")
    print()
    print("Please enter the diameter of the pizza in inches.")
    diam = eval (input("Diameter: "))
    print("Please enter the price of the pizza in euro.")
    price = eval (input("Price: "))
    r = diam/2
    pi = 3.141592653589793
    price_inch = price / (pi * (r * r))

    print("The price per square inch of the pizza is", price_inch, "euro.")

main()
