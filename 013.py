# Дана строка, найти второе вхождение буквы f
#если буква встречается только один раз, то вывести -1
# если не встречается ни разу, то -2
str_in = input('Enter string ')
find_char = 'f'
pos = str_in.find(find_char)
if pos == -1 :
    print(-2)
else:
    pos = str_in.find(find_char,pos+1)
    if pos == -1:
        print(-1)
    else:
        print(pos)