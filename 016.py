# дан список чисел. если в нем есть соседние эле-ты одного знака, то выведите их
# если соседних элементов одного знака нет - не выводите ничего
# если таких пар несколько, то выведите первую

input_list = list(map(int,input('Enter list ').split()))
previos = input_list[0]
flag = 0
for i in input_list[1::] :
 #   print(i)
    if flag != 1 and ((previos > 0 and i > 0) or (previos < 0 and i < 0)) :
        print(previos, i)
        flag = 1
    previos = i
