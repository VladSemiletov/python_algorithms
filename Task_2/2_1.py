print("Добро пожаловать. Знаки операций для работы: +, -, *, /.")
while True:
    try:
        
        operation = input('Введите знак операции(Для выхода введите 0): ')
        if operation == '0':
            break

        num1 = int(input('Введите первое число: '))
        
        num2 = int(input('Введите второе число: '))

    except ValueError:
        print('Неправильный ввод.')
        continue

    if operation == '0':
        break
    elif operation == '+':
        print(f'{num1} {operation} {num2} = {num1 + num2}')
    elif operation == '-':
        print(f'{num1} {operation} {num2} = {num1 - num2}')
    elif operation == '*':
        print(f'{num1} {operation} {num2} = {num1 * num2}')
    elif operation == '/':
        try:
            print(f'{num1} {operation} {num2} = {num1 / num2}')
        except ZeroDivisionError:
            print('Ошибка. Деление на ноль невозможно')
