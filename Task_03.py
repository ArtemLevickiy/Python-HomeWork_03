# Напишите программу, которая будет преобразовывать 
# десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

N = int(input('Введите число :'))
A = N
B = 1
Dv = 0
while A > 0:
    Dv = Dv + A % 2 * B
    B = B * 10
    A = A // 2
print(Dv)