"""
Повні квадрати
https://www.e-olymp.com/uk/problems/8918

Дано натуральне число n. Вивести в порядку зростання n перших
квадратів натуральних чисел.

Вхідні дані
Одне натуральне число n.
Вихідні дані
В одному рядку виведіть n перших квадратів натуральних чисел.

Вхідні дані #1
3
Вихідні дані #1
1 4 9
"""

# Зчитуємо вхідні дані і переводимо їх в ціле число
n = int(input())

# Пробігаємо по числам від '1' (включно) до 'n + 1' (не включно)
# Ці значення приймає змінна 'i'
for i in range(1, n + 1):
    # Знаходимо квадрат числа
    y = i**2
    # Друкуємо результат
    print(y, end=" ")
    # Ключовий параметр 'end=" "' вказує, що після друку змінної 'y',
    # буде встановлено пробіл замість переходу на новий рядок