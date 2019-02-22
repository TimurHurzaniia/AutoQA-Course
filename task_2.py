line = input('give me a string: ')
if len(line)%2 == 0:
    temp = line.split(line[len(line)//2])
    newline = line[len(line)//2] + temp[1] + temp[0]
    print(newline)
else:
    temp = line.split(line[len(line)//2 + 1])
    newline = line[len(line)//2 +1] + temp[1] + temp[0]
    print(newline)