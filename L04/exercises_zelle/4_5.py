def main():
    print("This program calculates the 'numeric value' of a name.")
    print()
    name = input("Enter a name: ")
    name = name.lower()
    x=0
    for letter in name:
        x = int(ord(letter)) + x - 96

    print("The 'numeric value' of the name is",format(x), ".")
main()
