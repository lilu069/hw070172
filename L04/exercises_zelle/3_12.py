def main():
    print("This program calculates the sum of the cubes of the first n natural numbers.")
    print()
    print("Please define n.")
    n = eval(input("Enter n: "))
    cube = 1
    for factor in range (2, n+1):
        cube = cube + factor ** 3
    print("The sum of the cube of the first", n, "natural numbers is", cube, ".")

main()
