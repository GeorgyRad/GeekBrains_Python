"""Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль."""

def division(first, second):
    try:
        return first / second
    except ZeroDivisionError:
        return "На ноль делить нельзя"
    except ValueError:
        return "Вы не ввели значение"
def division_use():
    print(division(int(input("Введите первое число: \n")))), (int(input("Введите второе число: \n")))
