#2. Напишите программу, которая на вход принимает 5 
# #чисел и находит максимальное из них.
#Ввод: любая коллекция значений типа <int>
#Вывод: значение типа <int>
my_list = [int(input('Введите число  ')),int(input('Введите число  ')),int(input('Введите число  ')),int(input('Введите число  ')),int(input('Введите число  '))]
# метод перебора
max = my_list [0] # переменная мах числа и присвоить 0 значение
for i in my_list: # тут перебираем
    if i>max: # и если i (это каждый элемент) будет больше мах
        i=max # тогда i = мах
print(max)