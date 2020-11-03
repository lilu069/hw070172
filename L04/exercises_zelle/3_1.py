def main():
    print("Calculate the volume and surface area of a sphere.")
    print()
    print("Please enter the radius in cm")
    r = eval(input("Radius: "))
    pi = 3.141592653589793
    volume = (4 / 3) * pi * (r * r * r)
    surface = 4 * pi * (r * r)

    print("The volume of the sphere is", volume, "cm³")
    print("The surface area of the sphere is", surface, "cm²")

main()
 
