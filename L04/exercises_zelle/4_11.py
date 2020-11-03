def main():
    print("This program illustrates a chaotic function")

    n = 10
    x = .25
    y = .26

    print("Index {0:>9}{1:>10}".format(x, y))
    print("--------------------")
    for i in range(n):
        x = 3.9 * x - 3.9 * x * x
        y = 3.9 * y - 3.9 * y * y
        print("{2:^3}{0:>12.5f}{1:>10.5f}".format(x, y, (i+1)))

main()
