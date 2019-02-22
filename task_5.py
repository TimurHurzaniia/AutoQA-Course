x = input('give me x: ')
y = input('give me y: ')
try:
    num1 = int(x)
    num2 = int(y)
except ValueError:
    z = str(x) + str(y)
    print(z)
else:
    z = num1 + num2
    print(z)