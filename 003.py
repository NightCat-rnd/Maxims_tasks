# дано целое четырехзначное число. Определите, является ли его десятичная запись симметричной
# если число меньше 4 знаков, то слева оно дополняется незначащими нулями
str_number = input('Введите число (максимум четырехзначное) ')
number_of_digit = len(str_number)
if number_of_digit == 1 :
    str_number = '000'+str_number
elif number_of_digit == 2 :
    str_number = '00'+str_number
elif number_of_digit == 3 :
    str_number = '0' + str_number
reverse_number = str_number[::-1]
#print(str_number, reverse_number)
if str_number == reverse_number :
    print('Число симметричное')
else:
    print('Число не симметричное')

