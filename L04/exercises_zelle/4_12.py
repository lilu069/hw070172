def main():
    print("This program calculates the future value of an investment.")

    principal = eval(input("Enter the amount of investment per year: "))
    apr = eval(input("Enter the annual interest rate: "))
    x = eval(input("Enter the number of years for the investment: "))
    summe = 0

    print("{0:<} {1:>10}".format("Year", "Value"))
    print("----------------")

    for i in range (x):
        principal = principal * (1 + .01 * apr)

        print("{0:>2}      ${1:<}.{2:0^2}".format(i+1, int(principal), int(principal%1 * 100)))

main()
