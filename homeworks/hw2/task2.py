"""Для списка реализовать обмен значений соседних элементов, т.е.
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input()."""

ask_list = input("введите спикок, через запятую \n")
list = ask_list.split(",")
counter = 0
for i in range(int(len(list) / 2)):
    list[counter], list[counter + 1] = list[counter + 1], list[counter]
    counter += 2
print(list)