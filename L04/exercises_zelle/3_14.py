def main():
    print("This program finds the average of numbers entered by you.")
    n = eval(input("How many numbers would you like to average? "))
    x = eval(input("Enter number: "))
    for factor in range (2, n+1):
        y = eval(input("Enter number: "))
        x = float(x) + float(y)
    print("The average of the given numbers is: ", x / n, ".")

main()
