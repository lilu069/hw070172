from graphics import *

def main():
    filename = input("Enter filename: ")
    infile = open(filename)

    #grab number of students and assign to numStud
    number = int(infile.number.append(int(line[:-1])))
    
    #grab name and grade and assign to lists studName and grade
    name = []
    grade = []
    lines = []
    for line in infile.readlines():
        x, y = line.split(": ")
        y = y[0:-1]
        name.append(x)
        grade.append(y)

    print(name)
    print(grade)
    
#initialize graphWin of size 400, (100 x numStud)
    win = GraphWin("Student Grade Chart", 400, 50 * number)

    #setCoords: -10, 0, 100, (10 x (numStud + 2))
    win.setCoords(-30, (10 * number + 2), 120, 0)

    #draw text studName
    for i in range (number):
        s = name[i].rjust(10)
        Text(Point(-20, 15 + number * .8 * i), s).draw(win)
    #draw Rectangle and clone
    for i in range (number):
        r = Rectangle(Point(0, 13 + number * .8 *i), Point(grade[i], 17 + number * .8 * i))
        r.draw(win)
#close file
    infile.close()
main()
