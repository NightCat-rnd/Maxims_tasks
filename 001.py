# Дано натуральное число, найти число десятков
number = int(input('Введите натуральное число'))
#математический способ
number_10 = number // 10 # избавляемся от единиц
tens = number_10 % 10 # остаток - десятки
print(f'Число десятков числа {number} = {tens}')
#через преобразование в строку
str_number = str(number)
print(f'Число десятков числа {number} = {str_number[-2]}')