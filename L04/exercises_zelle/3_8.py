def main():
    print("This program calculates the gregorian epact.")
    print()
    print("Please enter the year as a 4-digit number.")
    year = eval(input("Enter year: "))
    C = year//100
    epact = (8+(C//4)-C+((8*C+13)//25)+11*(year%19))%30

    print("The epact in the year", year, "is", epact, ".")

main()
