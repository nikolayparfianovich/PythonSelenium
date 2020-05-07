import random

n=int(input("Введите размер списка: "))
A=[]

if n in range (0,100):
    for i in range(n):
        a=random.random()
        A.append(a)
    print(A)
    print(min(A))

else:
    print("Введите другое число")