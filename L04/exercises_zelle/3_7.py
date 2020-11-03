import math 
def main():
    print("This program determines the distance between two points.")
    print()
    print("Please enter two coordinates.")
    x1,y1 = eval(input("Enter (x1,y1): "))
    x2,y2 = eval(input("Enter (x2,y2): "))
    distance = math.sqrt((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1))

    print("The distance between the points measures", distance, ".")
main()
