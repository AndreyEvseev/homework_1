# Задание 4. Напишите программу, которая по заданному номеру четверти, показывает диапазон 
# возможных координат точек в этой четверти (x и y).

import string


def check_correctness():
    correct = False
    while correct == False:
        quarter = int(input('Введите номер четверти, в которой расположена точка: '))
        if quarter > 0 and quarter <= 4:
            correct = True
        else:
            print('Некорректный номер четверти!')
    return quarter

def coordinates(quarter: int) -> string:
    str = None
    if quarter == 1:
        str = 'В 1-й четверти расположены точки с координатами: x > 0, y > 0.'
    elif quarter == 2:
        str = 'Во 2-й четверти расположены точки с координатами: x > 0, y < 0.'
    elif quarter == 3:
        str = 'В 3-й четверти расположены точки с координатами: x < 0, y < 0.'
    else:
        str = 'В 4-й четверти расположены точки с координатами: x < 0, y > 0.'
    return str

quarter = check_correctness()
str = coordinates(quarter)
print(str)
