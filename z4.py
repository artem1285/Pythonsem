# Напишите программу, которая будет 
# принимать на вход дробь и показывать первую цифру дробной части числа.

n = float(input('Введите n ')) # на вход получаем какое то число float
# a = n- int(n)
# b =int(a*10)
print(int (10*n)%10)