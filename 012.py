# Дана строка. если в строке f встречается один раз, то выведите ее индекс, если два и более - то индекс
# первого и последнего вхождения.
# Если символа нет, то ничего не выводить

str_in = input('Enter string ')
pos = str_in.find('f')
prnt = ''
if pos != -1 :
    prnt += str(pos)
rpos = str_in.rfind('f')
if rpos != 0 and rpos != pos :
    prnt += ' '+str(rpos)
print(prnt)
