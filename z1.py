#Напишите программу, которая принимает на вход два числа и 
#проверяет, является ли одно число квадратом другого.
a = int(input('Введите а '))
b = int(input('Введите b '))
print(a == b**2 or b == a**2)