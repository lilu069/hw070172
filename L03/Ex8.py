def main():
    print("This program calculates the total accumulation of an investment.")

    principal = eval(input("Enter the initial principal: "))
    rate = eval(input("Enter the annual interest rate: "))
    periods = eval(input("Enter the number of times the interest is compounded per year: "))
    
    for i in range(periods * 10):
        principal =  principal * (1 + rate/periods)

    print("The total accumulation of your investment in 10 years is:", principal)
    
main()
