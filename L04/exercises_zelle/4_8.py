def main():

#Get plaintext(p_text) and key(x) from the user
    message = input("Enter the message you'd like encrypted: ")
    key = eval(input("What's the key? : "))

    message = message.lower()
    
#Create string of letters
    table = "abcdefghijklmnopqrstuvwxyz"

#Convert plaintext to ciphertext(c_text) using cipher loop
    ciphertext = ""
    for ch in message:
        ciphertext = ciphertext + (table[((ord(ch)) - 97) + key % 52])

    print("The encoded message is", format(ciphertext))

main()
