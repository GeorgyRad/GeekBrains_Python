"""Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict."""

# Реализация через list

ask_mounth = input("введите месяц \n")
list = int(ask_mounth)
mounths = ('Зима', 'Весна', 'Лето', 'Осень')
season = list // 3 % 4
print(mounths[season])

# Реализация через dict

mounth = int(input("введите месяц \n"))
seasons = {
    "Зима": (12, 1, 2),
    "Весна": (3, 4, 5),
    "Лето": (6, 7, 8),
    "Осень": (9, 10, 1)
}
person = {}
for key, number in seasons.items():
    if mounth in number:
        print(key)
        break
