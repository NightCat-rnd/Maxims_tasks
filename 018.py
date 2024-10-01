list_in = [1,2,3,4,5]
print('List: ',list_in)
print('Четные индексы:',list_in[::2])
#-------------
list_in = [1,2,3,2,1]
print('List: ',list_in)
print('Мах =',max(list_in))
#------------
list_in = [1,2,3,4,5]
print('List: ',list_in)
print('в обратном порядке:',list_in[::-1])
#-------------
list_in = [1,2,3,4,5]
print('List: ',list_in)
for i in range(0,len(list_in)-1,2) :
    list_in[i], list_in[i+1] = list_in[i+1], list_in[i]
print('Переставлены соседние:',list_in)
#--------------



