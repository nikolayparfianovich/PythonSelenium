#вариант 2
value = int(input("Введите значение P: "))
value_2 = int(input("Введите значение Q: "))
A=[]

while value < value_2:
    value = value * 1.03
    A.append(value)
print("Выручка будет {} в тот день, когда P превысит Q ".format(value))
days = (len(A))
print("На это потребуется {} дней".format(days))