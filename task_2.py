##triangle
a, b = 179, 971
c = ((a**2) + (b**2))**(1/2)
print(c)
## two digits num
a = input('give me please two digits num: ')
print(int(a)//10)
## three digits num sum
a = input('give me please three digits num: ')
sum = 0
for i in a:
    sum += int(i)
print(sum)
## next even
n = int(input('give me please integer num: '))
if n%2 == 0:
    print(' is alredy even')
else:
    while True:
        n += 1
        if n%2 == 0:
            print(n)
            break
## fraction part extraction
x = float(input('give me please any num: '))
y = str(x - int(x))
print(y[2:])
## first figure after dot
x = float(input('give me please any num: '))
y = str(x - int(x))
print(y[2])