def main():
    print("This program calculates the average word length in a sentence.")
    text = input("Enter a sentence: ")
    words = []

    for string in text.split():
        x = string[0]
        words.append(x)             

    length = 0
    for string in text.split():
        length = len(string) + length
        average = length/(len(words))

    print("The average word length is", average, ".")

main()
