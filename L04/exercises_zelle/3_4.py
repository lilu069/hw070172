def main():
    print("This program determines the distance to a lightning strike based on")
    print("the time elapsed between the flash and the sound of thunder.")
    print()
    print("Please enter the seconds elapsed between the flash and the sound of thunder.")
    time = eval(input("seconds: "))
    distance = (time * 1100) / 5280
    
    print("The distance to the lightning strike equals", distance, "miles.")

main()
