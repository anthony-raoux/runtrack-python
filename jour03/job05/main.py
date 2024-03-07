def calcule(num1, operator, num2):
    if (operator == '+'):
        print(num1 + num2)
    if (operator == '-'):
        print(num1 - num2)
    if (operator == '*'):
        print(num1 * num2)
    if (operator == '/'):
        print(num1 / num2)
    if (operator == '%'):
        print(num1 % num2)

calcule(5, '+', 5)
calcule(10, '-', 6)
calcule(5, '*', 3)
calcule(6, '/', 3)
calcule(10, '%', 3)

