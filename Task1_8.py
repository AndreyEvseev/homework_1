# Задание 8. Найти наибольший простой делитель числа

n = int(input('Введите натуральное число N: '))
simple_divisor = 1
for i in range(2, n):
    if n % i == 0:
        j = 2
        while i % j != 0 or j == n - 1:
            j += 1
        if j == i:
            simple_divisor = i
    else:
        continue
print(f'Наибольший простой делитель числа {n} = {simple_divisor};')    

