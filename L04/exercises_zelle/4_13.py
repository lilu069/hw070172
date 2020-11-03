def main():
    filename = input("Enter filename: ")
    infile = open(filename)
    data = infile.read()

    #initialize output list
    words = []

    #loop for duration of input list split
    for string in data.split():
        #create a temporary variable to store the first
        #letter of each word
        x = string[0]
        words.append(x)

    letters = 0
    for string in data.split():
        letters = len(string) + letters
        average = letters / (len(words))
 
    print("The average word lenth is", format(average), ".")
    print("The total amount of letters is", format(letters), ".")
    print("The number of words is", format(len(words)), ".")
main()
