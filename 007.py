# по данному N вычислите 1**2+2**2 + ... + N**2
number = int(input('Введите целое число '))
result = 0
for i in range(1, number+1) :
    result += i**2
print(result)