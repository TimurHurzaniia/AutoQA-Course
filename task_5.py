list = []
for i in range(3):
    a = input('give me num: ')
    list.append(a)
newlist = sorted(list)
for i in newlist:
    print(i,end=' ')