import math
def main():
    print("This program caclculates the area of a triangle given the length of its three sides.")
    print()
    print("Please enter the length of the three sides in cm.")
    a = eval(input("Enter a: "))
    b = eval(input("Enter b: "))
    c = eval(input("Enter c: "))

    s = (a+b+c)/2
    area = math.sqrt(s*(s-a)*(s-b)*(s-c))

    print("The area of the triangle equals", area, "cm²")

main()
