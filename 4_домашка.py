with open("C:\development\Test\exemple.txt") as file:
    for line in file.readlines():
        x = line.split()
        for i in x:
            if i.startswith('A'):
                a=(",".join(x))
                print(a)
                new = open("exemple_2.txt","w")
                new.write(a)
                a=a.split(",")
                print(len(a))





























