import math as m
def main():
    print("This program computes the Fibonacci numer n, choosed by the user.")
    n = eval(input("Which number of the Fibonnaci sequence should be shown?: "))
    x = 1
    y = 0

    for i in range (n):
        z = x + y
        x = y
        y = z
    print("The ",n,"th Fibonacci number is", y, ".")
main()
