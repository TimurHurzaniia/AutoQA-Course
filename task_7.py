f = open('text_task_7.txt')
text = f.read()
#1
num_words = len(text.replace('\n', ' ').split(' '))
print(num_words)
##2
clear_text = ''.join(i for i in text if i not in ['.', ',', '!'])
print(clear_text)
##3
sorted_clear_text = sorted(clear_text.replace('\n', ' ').split(' '))
print(' '.join(sorted_clear_text))
##4**
d = {}
for i in sorted_clear_text:
    d[i] = sorted_clear_text.count(i)
print(d)
f.close()