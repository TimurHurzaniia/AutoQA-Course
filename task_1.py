s = input('give me a string no less than 3 chars length: ')
try:
    print(s[2], s[-2], s[:5], s[:-2], s[::2], s[1::2], s[::-1], s[-1:0:-2], s[-2:0:-1], sep='\n')
except IndexError:
    print('!!!Given string is to short!!!')