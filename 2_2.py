number = input('Введите число: ')
even = 0
odd = 0
for j in number:
    i = int(j)
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
print(f'У числа {number}: четных цифр - {even}, нечетных - {odd} ')