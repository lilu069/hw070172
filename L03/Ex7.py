def main():
    print("This program calculates the total accumulation of an investment.")

    principal = eval(input("Enter the amount of investment per year: "))
    apr = eval(input("Enter the annual interest rate: "))
    x = eval(input("Enter the number of years for the investment: "))
    summe = 0

    for i in range(x):
        summe = (summe + principal) * (1 + apr)

    print("The total accumulation of your investment is:", summe)
    
main()
