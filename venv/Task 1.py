number = int(input("Введите число: "))

if number in range (0,8):
    if number ==0:
        print("Zero")
    elif number ==1:
        print("One")
    elif number ==2:
        print("Two")
    elif number ==3:
        print("Three")
    elif number ==4:
        print("Four")
    elif number ==5:
        print("Five")
    elif number ==6:
        print("Six")
    elif number ==7:
        print("Seven")
else:
    print("Choose another value")