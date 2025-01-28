from math import sqrt

message = 'Добро пожаловать в самую лучшую программу для вычисления ' \
          'квадратного корня из заданного числа'
print(message)


def CalculateSquareRoot(Number):
    """Вычисляет квадратный корень."""
    return sqrt(Number)


def calc(your_number):
    """Вычисляет квадратный корень из введенного вами числа."""
    if your_number <= 0:
        print('Пожалуйста, введите положительное число.')
        return
    result = CalculateSquareRoot(your_number)
    print(f'Мы вычислили квадратный корень из введённого вами числа.'
          f'Это будет: {result}')
