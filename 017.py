# дан список чисел. выведите все элементы списка, которые больше предыдущего

input_list = list(map(int,input('Enter list ').split()))
previos = input_list[0]
out_list = ''
for i in input_list[1::] :
    if i > previos :
        out_list = out_list +str(i) + ' '
    previos = i
print(out_list)
