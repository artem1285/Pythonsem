# Натуральное число, где сумма всех цифр слева от середины равна сумме
# всех цифр справа, называется сбалансированным. Если количество цифр в числе нечётное,
# то считаются суммы слева и справа от средней цифры. Задача: определить,
# является ли натуральное число сбалансированным.

# Ввод: значения типа <int>
# Вывод: значения типа <bool>
# Примеры:
# 12321
# True
# 1234
# False
# 5344
# True
num = input('Введите натуральное число: ') # принимаем число ввидес троки

#Далее что бы найти сумму слева и справа пишем  
sum_1 = 0
sum_2 = 0  
#  и тогда в цикле for
# создаем список
for i in range(0, len(num) // 2):
    sum_1+=int(num[i]) # это суммируем первые индексы
    sum_2+=int(num[-i]) # это суммируем втрорыек но уже отрицательные индексы
print(sum_1 == sum_2)