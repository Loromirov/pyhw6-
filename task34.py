# # Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
# # Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, 
# # Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов 
# # (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. 
# # Фраза может состоять из одного слова, если во фразе несколько слов, 
# # то они разделяются дефисами. Фразы отделяются друг от друга пробелами. 
# # Стихотворение  Винни-Пух вбивает в программу с клавиатуры. 
# # В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке

def rythm(str):
    str = str.split()
    list1 = []
    for word in str:
        count = 0
        for i in word:
            if i in "АЯУЮОЕЁЭИЫ":
                count += 1
        list1.append(count)
    return len(list1) == list1.count(list1[0])
n = 'пара-ра-рам рам-пам-папам па-ра-па-дам'
n = n.upper()
if rythm(n):
    print(True)
else:
    print(False)