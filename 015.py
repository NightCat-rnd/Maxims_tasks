# найдите кол-во положительных (>0) элементов списка
input_list = list(map(int,input('Enter list: ').split()))
sum = 0
for i in input_list:
    if i>0:
        sum += 1
print(sum)
