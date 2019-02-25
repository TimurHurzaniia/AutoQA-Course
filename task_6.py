##1
def is_year_leap(a):
    if a % 400 == 0:
        print('Yes')
    elif a % 4 == 0 and a % 100 != 0:
        print('Yes')
    else:
        print('No')
n = input('give me please integer num: ')
try:
    n = int(n)
except ValueError:
    print('Not integer is given')
else:
    is_year_leap(n)

##2
def triangle_check(sides):
    temp = sides.pop(sides.index(max(sides)))
    if sum(sides) > temp:
        print('Yes')
    else:
        print('No')

sides_list = []
for i in range(3):
    x = input('give me lenght of the side {}: '.format(i))
    try:
        a = int(x)
    except ValueError:
        print('!!!Not integer is given!!!')
    else:
        sides_list.append(a)
triangle_check(sides_list)
##3
def input_repeat():
    while True:
        s = input('input a string please without spaces inside: ')
        if ' ' not in s[1:-1]:
            break
    return s

input_repeat()
##4
def simple_input():
    while True:
        s = input('input an integer please: ')
        try:
            i = float(s)
        except ValueError:
            continue
        else:
            return i
            break

##5

sides = []
for i in range(3):
    sides.append(simple_input())

def triangle_type(listsides):
    max_side = listsides.pop(listsides.index(max(sides)))
    if sum(listsides) > max_side:
        if max_side**2 == listsides[0]**2 + listsides[1]**2:
            print('rectangular triangle exists')
        elif max_side**2 > listsides[0]**2 + listsides[1]**2:
            print('obtuse angled triangle exists')
        elif max_side **2 < listsides[0]**2 + listsides[1]**2:
            print('acute-angled triangle exists')
    else:
        print('triagle could not be built')

triangle_type(sides)

##6
def distance(x1,y1,x2,y2):
    d = ((x2-x1)**2 + (y2-y1)**2)**1/2
    return d

x1 = simple_input()
y1 = simple_input()
x2 = simple_input()
y2 = simple_input()

print(distance(x1, y1, x2, y2))