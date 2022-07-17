# Задание 6. Найти факториал числа

n = int(input('Задайте натуральное число N: '))
fact = 1
for i in range(2, n+1):
    fact = fact * i
print(f'{n}! = {fact};')
