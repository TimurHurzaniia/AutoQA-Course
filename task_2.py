#from lection slide 9
with open('doc_1.txt') as input_file:
    with open('doc_2.txt','w') as output_file:
        n = 0
        for line in input_file:
            n+= 1
            output_file.write(str(n) + ': ' + line)
#input_file.close()
#output_file.close()

#from lection slide 10
input_file = open('doc_1.txt')
try:
    i = int(input_file.read())
except ValueError:
    print('Could not be converted to int')
else:
    print('I did it!')
finally:
    input_file.close()
