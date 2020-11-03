def main():
    print("This program calculates the lines, words and characters in a file.")
    filename = input("Enter filename: ")
    infile = open(filename)
    data = infile.read()
    words = []
    letters = 0

    for string in data.split():
        x = string[0]
        words.append(x)
        letters = len(string) + letters
    infile.close()

    infile = open(filename)
    linesf = infile.readlines()

    lines = []
    for line in linesf:
        lines.append(line)
    print("The mumber of lines in the file is", format(len(lines)), ".")
    print("The number of letters is", format(letters),".")
    print("The number of words is", format(len(words)),".")
    infile.close()
main()
