def main():
    print("This program creates an acronym out of a sentence.")
    print()
    sentence = input("Enter a sentence: ")
    words = []
    for string in sentence.split():
        x = string[0].upper()
        words.append(x)

    acronym = "".join(words)
    print("The acronym for the sentence is:", acronym, ".")
main()
