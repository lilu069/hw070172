import math as m

def main():
    print("This program computes square roots with the Newton method.")
    x = eval(input("Enter a value to find the squareroot of: "))
    y = eval(input("How many times should Newton's formula be iterated?: "))

    g = x / 2

    for i in range (y):
        g = (g + x / g) / 2
    print("The final value of the guess is:", g, ".")
    print("The difference to the value of math.sqrt(x) is:", m.sqrt(x)-g,".")
main()
