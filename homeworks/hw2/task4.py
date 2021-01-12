'''Пользователь вводит строку из нескольких слов, разделённых пробелами.
Вывести каждое слово с новой строки. Строки нужно пронумеровать.
Если слово длинное, выводить только первые 10 букв в слове.'''

some_string = input("введите фразу \n")
developed_string = some_string.split(" ") # тут я решил разбить строку на отдельные
#print(developed_string[1])
for num, word in enumerate(developed_string):
    print(f'{num}: {word[:10]}')