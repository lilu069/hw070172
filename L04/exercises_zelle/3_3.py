def main():
        print("This program calculates the molecular weight of a carbohydrate")
        print("based on the number of hydrogen, carbon, and oxygen atoms in the molecule.")
        print()
        print("Please enter the number of atoms.")
        H = eval (input("Hydrogen: "))
        C = eval (input("Carbon: "))
        O = eval (input("Oxygen: "))

        total_weight = H * 1.00794 + C * 12.0107 + O * 15.9994

        print("The molecular weight of this carbohydrate is", total_weight, "grams/mole.")

main()
