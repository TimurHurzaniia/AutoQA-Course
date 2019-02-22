##1
a = 0
while a!= 11:
    print(a)
    a += 1
##2
a = 20
while a!= -1:
    print(a, end=' ')
    a -= 1
##3
a = 1000
temp = 1
n = 0
while True:
    a //= 2
    n += 1
    temp = a%2
    if temp != 0:
        break
print('\n', n)