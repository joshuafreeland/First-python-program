"""joshua Calculator"""
def addition ():
    print("Addition")
    b = float(input("Enter number"))
    c = 0 
    ans = 0
    while b != 0:
        ans = ans + b
        c+=1
        b = float(input("Enter the next number (0 to calculate): "))
    return [ans,c]
def subtraction ():
    print("Subtraction")
    b = float(input("Enter the number: "))
    c = 0 
    sum = 0
    while b != 0:
        ans = ans - b
        c+=1
        b = float(input("Enter the next number (0 to calculate): "))
    return [ans, c]
def average():
    an = []
    an = addition()
    b = an[1]
    c = an[0]
    ans = a / c
    return [ans,t]

while True:
    list = []
    print(" My fist python program!")
    print(" Enter 'a' for addition")
    print(" Enter 's' for subtraction")
    print(" Enter 'm' for multiplication")
    print(" Enter 'v' for average")
    print(" Enter 'q' for quit")
    c = input (" ")
    if c != 'q':
        if c == 'a':
            list = addition()
            print("Ans = ", list[0], " total inputs ", list[1])
        elif c == 's':
            list = subtraction()
            print("Ans = ", list[0], " total inputs ", list[1])
        elif c == 'm':
            list = multiplication()
            print("Ans = ", list[0], " total inputs ", list[1])
        elif c == 'v':
            list = average ()
            print("Ans = ", list[0], " total inputs ", list[1])
        else:
            print("invalid entry")
    else:
        break




