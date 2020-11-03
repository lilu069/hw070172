def main():
    print("This program calculates the 'numeric value' of a name.")
    print()
    name = input("Enter a name: ")
    name = "".join(name)
    name = name.lower()
    name = name.lstrip()
    name = name.replace(" ", "`")
    name = name.replace("-", "`")
    
    x = 0
    for letter in name:
        x = int(ord(letter)) + x - 96

    print("The 'numeric value' of the name is",format(x), ".")
main()
