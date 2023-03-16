import time

time.sleep(1)
print ("|" * 1)
print ("")
print ("""Что выведет данная строка?
>>>'1'+'2'

Для справки введи комманду:help  
""")
answer_1 = str(input("Enter your answer: "))
while (True):
    if answer_1 == "'12'":
        print("Это правельный ответ, поехали дальше")
        break
    if answer_1 == 'help':
        print("""
>>>'spam' * 3
'spam spam spam'
>>> 'a' + 'b'
'ab'
>>>'a'+'-'+'a'+'-'+'a'
a-a-a
Эта штука называется Конкатенация строк — операция присоединения, «склеивания» символов или их наборов.
Операция конкатенации строк возможна не только с помощью оператора *, но и с помощью
оператора +. Также их можно использовать вместе. Это всё из-за ковычек. Вообще пользуйся
helpом чаще.""")
        print("")
        print ("""Что выведет данная строка?
>>>'1'+'2'""")
        answer_1 = str(input("Enter your answer: "))
    else:
        print("Попробуй ещё раз, ты забыл про кавычки бро")
        answer_1 = str(input("Enter your answer: "))
    
time.sleep(1)
print ("|" * 2)
print ("")
print ("""Python-ну в строке нужны разные ковычки, что я имею ввиду
Вот так не Работает:

>>> "Хотим двойные кавычки! Python, выведи "Москва". Пожалуйста!"
SyntaxError: invalid syntax

А так работает:

>>> 'Москва не подсвечивается зеленым цветом. А это значит, что Python видит только строки между одинарными кавычками или между двойными. "Попробуем совместить"'
'Москва не подсвечивается зеленым цветом. А это значит,
что Python видит только строки между одинарными кавычками или между двойными. "Попробуем совместить"'

>>> "Получилось! А если 'внутри' предложения взять одинарные кавычки, а снаружи - двойные?"
"Получилось! А если 'внутри' предложения взять одинарные
кавычки, а снаружи - двойные?"

Так не работает:

>>> 'А если все одинарные'?':'
SyntaxError: invalid syntax

Чтобы продолжить введи комманду: next

Для справки введи комманду: help  
""")
answer_1 = str(input("Enter your answer: "))
while (True):
    if answer_1 == 'next':
        print("поехали дальше")
        break
    if answer_1 == 'help':
        print("""Тут ничего нет)))
""")
        print("")
        print ("""Напиши next""")
        answer_1 = str(input("Enter your answer: "))
    else:
        print("Напиши next")
        answer_1 = str(input("Enter your answer: "))

time.sleep(1)
print ("|" * 3)
print ("")
print ("""Какую переменную нужно вставить в функцию print(...), чтобы появилась надпись Hello gnome?:
a = input("Enter your answer: Hello gnome")
print(...)

Для справки введи комманду:help  
""")
answer_1 = str(input("Enter your answer: "))
while (True):
    if answer_1 == "a":
        print("Это правельный ответ, поехали дальше")
        break
    if answer_1 == 'help':
        print("""функция input() ожидает ввода данных с клавиатуры после
комментария для пользователя до нажатия клавиши Enter,
причем все данные записываются как строка символов (это
очень важно!)""")
        print("")
        print ("""Какую переменную нужно вставить в функцию print(...), чтобы появилась надпись Hello gnome?:
a = input("Enter your answer: Hello gnome")
print(...)

Для справки введи комманду:help """)
        answer_1 = str(input("Enter your answer: "))
    else:
        print("Попробуй ещё раз, ты забыл про кавычки бро")
        answer_1 = str(input("Enter your answer: "))


time.sleep(1)
print ("|" * 4)
print ("")
print ("""Какой из представленных значение можно вывести с помощmю этого кода,
a = int(input("Enter your age: "))
Значения:
18
ф
f
KUY

Для справки введи комманду:help  
""")
answer_1 = str(input("Enter your answer: "))
while (True):
    if answer_1 == "18":
        print("Это правельный ответ, поехали дальше")
        break
    if answer_1 == 'help':
        print(""" функция int() преобразует строку, введенную с клавиатуры,
в целое число """)
        print("")
        print ("""Какой из представленных значение можно вывести с помощmю этого кода,
a = int(input("Enter yout age: "))
Значение
18
ф
f
KUY

Для справки введи комманду:help  """)
        answer_1 = str(input("Enter your answer: "))
    else:
        print("Попробуй ещё раз, ты забыл про кавычки бро")
        answer_1 = str(input("Enter your answer: "))
    
time.sleep(1)
print ("|" * 5)
print ("")
print ("""Какой из представленных значение можно вывести с помощmю этого кода,
a = float(input("Enter your age: "))
Значения:
1.8
ф
f
KUY

Для справки введи комманду:help  
""")
answer_1 = str(input("Enter your answer: "))
while (True):
    if answer_1 == "1.8":
        print("Это правельный ответ, поехали дальше")
        break
    if answer_1 == 'help':
        print(""" функция float() преобразует строку, введенную с клавиатуры,
в дробное число """)
        print("")
        print ("""Какой из представленных значение можно вывести с помощmю этого кода,
a = float(input("Enter yout age: "))
Значение
1.8
ф
f
KUY

Для справки введи комманду:help  """)
        answer_1 = str(input("Enter your answer: "))
    else:
        print("Попробуй ещё раз, ты забыл про кавычки бро")
        answer_1 = str(input("Enter your answer: "))