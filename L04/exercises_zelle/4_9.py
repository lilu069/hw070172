def main():
    print("This program counts the words in a sentence.")
    text = input("Write sentence: ")

    word_len = []

    for string in text.split():
        x = string[0]
        word_len.append(x)

    print("The wordcount of the sentence is", len(word_len), ".")

main()
