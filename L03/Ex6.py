def main():
    print("This program calculates the future value of an investment.")
    print("You can define the number of years considered")

    principal = eval(input("Enter the inicial principal: "))
    apr = eval(input("Enter the annual interest rate: "))
    x = eval(input("Enter the number of years for the investment: "))

    for i in range(x):
        principal = principal * (1 + apr)

    print("The value in", x, "years is:", principal)

main()
