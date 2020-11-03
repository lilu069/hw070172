def main():
    print("This program converts a date in form mm/dd/yyy to month, day, year.")
    mdy = eval(input("Enter a date (mm/dd/yyy): "))

    months = ["January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"]

    monthStr = months[month-1]

    print("The converted date is {1}/{0}/{2}, or {3} {0},{2}").format(mdy, monthStr)

main()
