def main():
    print("This program sums a series of numbers entered by the user.")
    n = eval(input("How many numbers should be summed? "))
    x = eval(input("Enter number: "))
    for factor in range (2, n+1):
        y = eval(input("Enter number: "))
        x = x + y
    print("The sum is", x, ".")

main()
