# Напишите программу, которая принимает на вход число 
# и проверяет, кратно ли оно 5 и 10 или 15, но не 30

n = float(input('Введите n ')) # на вход получаем число float
print((n % 5 == 0 and n % 10 == 0 or n % 15 == 0) and n % 30 != 0)  # выводит типа bool. остаток от деления должен быть равен 0, а где 30 не равно 0