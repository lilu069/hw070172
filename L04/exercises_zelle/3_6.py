def main():
    print("This program calculates the slope of a line through two (non-vertical)points.")
    print()
    print("Please enter two coordinates (x1, x2) and (y1, y2).")
    x1 = eval (input("x1: "))
    x2 = eval (input("x2: "))
    y1 = eval (input("y1: "))
    y2 = eval (input("y2: "))
    slope = (y2 - y1) / (x2 - x1)

    print("The slope measures", slope,".")
main()
