def main():
    print("This program calculates the sum of the first n natural numbers.")
    print()
    print("Please define n.")
    n = eval(input("Enter n: "))
    summe = sum(range(n+1))

    print("The sum of the first", n, "natural numbers is", summe, ".")

main()
