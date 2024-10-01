from collections import deque
list_in = [1,2,3,4,5]
print('List: ',list_in)
rotaded_list = list_in[4:]+list_in[:4]
print('Циклический сдвиг вправо:',rotaded_list)
my_list = deque(list_in)
my_list.rotate(1)
print('Циклический сдвиг вправо:',my_list)
#--------------
list_in = [7,6,5,4,3,2,1,2]
print('List: ',list_in)
list_in.pop()
print('удален последний эдемент:',list_in)
