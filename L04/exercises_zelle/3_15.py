import math
def main():
    print("Thos program approximates the value of pi.")
    n = eval(input("Enter how many terms should be summed: "))
    x = 0
    m = 1
    for i in range(1, 2 * n + 1, 2):
        x = x + (m * 4/i)
        m = -m
    print("The final approximation based on the choosed terms is", x,".")
    print("The difference of the approximation to math.pi is", math.pi - x, ".")
main()
