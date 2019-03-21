with open('doc_3.txt') as input_file:
    with open('doc_4.txt', 'a') as output_file:
        word_list = sorted(input_file.read().split())
        word_dict = {}
        for i in word_list:
            word_dict[i] = word_list.count(i)
        for i in word_dict.keys():
            output_file.write('/{}/ word is contained {} times\n'.format(i, word_dict[i]))





