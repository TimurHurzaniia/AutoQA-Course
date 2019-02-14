sides = []
for i in range(3):
    a = int(input('give me lenght of the side {}: '.format(i)))
    sides.append(a)
temp = sides.pop(sides.index(max(sides)))
if sum(sides) > temp:
    print('Yes')
else:
    print('No')