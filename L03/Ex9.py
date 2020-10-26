def main ():
    print("This program helps you to convert degrees Fahrenheit into degrees Celsius")
    fahrenheit = eval(input("What is the Fahrenheit temperature? "))
    celsius = (fahrenheit - 32) * 5/9
    print("The temperature is", celsius, "degrees Celsius.")
main()
