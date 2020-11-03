import math
def main():
    print("This program calculates the length of a ladder required")
    print("to reach a given height while leaned against a house.")
    print()
    print("Please enter the height (in m) and angle (in degrees) of the ladder.")
    height = eval(input("Enter height: "))
    angle = eval(input("Enter angle: "))
    pi = 3.141592653589793
    angle_radians = (pi/180)*angle
    length = height/math.sin(angle_radians)

    print("The length of the ladder has to be", length, "m.")
main()
