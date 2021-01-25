"""Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""
numbers = input("Введите 3 числа \n")

def my_func(a, b, c):
    number = [a, b, c]
    number.remove(min(a, b, c))
    return sum(number)

def my_func_use():
    print(my_func(numbers))
