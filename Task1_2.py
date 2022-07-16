# Задание 2. Напишите программу дляпроверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

identity = True
for x in True, False:
    for y in True, False:
        for z in True, False:
            print(f'{x = } {y = } {z = }         result: {not(x or y or z) == (not x and not y and not z)}')
print(f'{identity = }')
