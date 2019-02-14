line = input('give me a line, please: ')
for i in line:
    if i.isdigit():
         print('yes '+ i + ' is digit')
print(line.count(' '))
print(line.count('.'))
line_1 = 'Homework'
temp_line = line_1.rjust((100 - len(line_1))//2)
print(temp_line.ljust((100 - len(line_1))//2))
line_2 = 'eat, sleep, rave, repeat'
print(line_2.title())