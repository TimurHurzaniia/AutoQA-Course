#1
l = [1,2,3,4,5,6]
while l:
    temp = l.pop(0)
    print(temp)
    print(l)
#2**
line = 'qwerty'
n = len(line)
i = 0
while True:
    line = line[1::]
    i += 1
    print(line)
    if i == n:
        break
##3
m = [3,5,7,9,1,8,2]
m.sort(reverse=True)
while m:
    temp = m.pop(0)
    print(temp)
    print(m)
