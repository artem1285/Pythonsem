# Напишите программу, которая принимает на вход число N и выдаёт
# следующую последовательность из N членов: 1, -3, 9, -27, 81, …
# это геометрическая прогрессия

num = int(input("введите число: "))
# num - это число которое будет показывать количество итераций
for i in range(num):
    print((-3)**i, end=" ")  # степень -3* на число
