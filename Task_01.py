# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, 
# второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

list_1 = list(map(int, input("Введите числа через пробел:\n").split()))
indexA = 0
indexB = -1
while list_1[indexA] <= list_1[indexB]:
    print(list_1[indexA] * list_1[indexB])
    indexA += 1
    indexB -= 1