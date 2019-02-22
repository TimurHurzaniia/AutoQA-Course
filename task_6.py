##1
n = input('give me please integer num: ')
try:
    n = int(n)
except ValueError:
    print('Not integer is given')

else:
    def is_year_leap(a):
        if a % 400 == 0:
            print('Yes')
        elif a % 4 == 0 and a % 100 != 0:
            print('Yes')
        else:
            print('No')

    is_year_leap(n)
##2
def triangle_check():
    sides = []
    for i in range(3):
        x = input('give me lenght of the side {}: '.format(i))
        try:
            a = int(x)
        except ValueError:
            print('!!!Not integer is given!!!')
        else:
            sides.append(a)
    temp = sides.pop(sides.index(max(sides)))
    if sum(sides) > temp:
        print('Yes')
    else:
        print('No')
triangle_check()
##3
def input_repeat():
    while True:
        s = input('input a string please without spaces inside: ')
        if ' ' not in s[1:-1]:
            break

input_repeat()
##4
def input_repeat():
    while True:
        s = input('input an integer please: ')
        try:
            i = int(s)
        except ValueError:
            continue
        else:
            break

input_repeat()
##5
def triangle_type():
    a = int(input('give me a length a: '))
    b = int(input('give me a length b: '))
    c = int(input('give me a length c: '))
    sides = [a, b, c]
    max_side = sides.pop(sides.index(max(sides)))
    if sum(sides) > max_side:
        if max_side**2 == sides[0]**2 + sides[1]**2:
            print('rectangular triangle exists')
        elif max_side**2 > sides[0]**2 + sides[1]**2:
            print('obtuse angled triangle exists')
        elif max_side **2 < sides[0]**2 + sides[1]**2:
            print('acute-angled triangle exists')
    else:
        print('triagle could not be built')

triangle_type()
##6
def distance(x1,y1,x2,y2):
    d = ((x2-x1)**2 + (y2-y1)**2)**1/2
    return d

x1 = int(input('give me an integer X1: '))
y1 = int(input('give me an integer Y1: '))
x2 = int(input('give me an integer X2: '))
y2 = int(input('give me an integer Y2: '))

print(distance(x1, y1, x2, y2))