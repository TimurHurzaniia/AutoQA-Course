list = []
for i in range(3):
    a = input('give me num: ')
    list.append(a)
if list.count(list[0]) == 3:
    print('3')
elif list.count(list[0]) == 2:
    print('2')
else:
    print('0')