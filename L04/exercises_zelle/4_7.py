def main():

    message = input("Enter the message you'd like encrypted: ")
    key = eval(input("What's the key? : "))

    ciphertext = ""
    for ch in message:
        ciphertext = ciphertext + (chr(ord(ch) + key))

    print("The encoded message is", format(ciphertext))

main()
