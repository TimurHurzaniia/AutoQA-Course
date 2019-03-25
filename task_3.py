import string
from collections import Counter

with open('doc_3.txt') as input_file:
    with open('doc_4.txt', 'w') as output_file:
        cut = set(string.punctuation)
        clear_text = ''.join(ch for ch in input_file.read() if ch not in cut)
        word_list = sorted(clear_text.split())
        '''word_dict = {}
        for i in word_list:
            word_dict[i] = word_list.count(i)'''
        word_dict  = Counter(word_list)
        for i in word_dict:
            output_file.write('/{}/ word is contained {} times\n'.format(i, word_dict[i]))





