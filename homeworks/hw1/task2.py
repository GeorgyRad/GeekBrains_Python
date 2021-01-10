"""Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк."""

# Вариант 1

ask_time = input("Введите время в секундах: \n")
sec = ask_time
if sec.isdigit():
    if int(sec) >= 60:
        min = int(sec) // 60
        sec = int(sec) % 60
    else:
        print("00:00:", sec, sep="")
else:
    print('Введите кол-во секунд цифрами')
if int(min) >= 60:
    hour = int (min) // 60
    min = int(min) % 60
    print(hour, ":", min, ":", sec, sep="")
else:
    print ("00:", min, ":", sec, sep="")



# Вариант 2
sec_inp = int(input('Введите кол-во секунд: \n'))
hour = sec_inp // 3600
min = (sec_inp // 60) % 60
sec = (sec_inp ) % 60
if hour < 10:
    hour = "0" + str(hour)
else:
    hour = str(hour)
if min < 10:
    min = '0'+str(min)
else:
    min = str(min)
if sec < 10:
    sec = '0'+str(sec)
else:
    sec = str(sec)
print(hour, ":", min,":", sec, sep= "")