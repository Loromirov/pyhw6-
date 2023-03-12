# # Задача 32: Определить индексы элементов массива (списка), 
# # значения которых принадлежат заданному диапазону (т.е. не меньше 
# # заданного минимума и не больше заданного максимума)
import random

n = int(input("введите длинну массива: "))
list1 = []
for i in range(n):
    list1.append(random.randint(0, 10))
print(list1)
minIn = int(input("введите минимальное число диапозона: "))
maxIn = int(input("введите максимальное число диапозона: "))

for i in range(len(list1)):
    if minIn < list1[i] < maxIn:
        print(i, end = ' ')