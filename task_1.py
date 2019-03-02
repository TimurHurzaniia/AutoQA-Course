def song_generator(lines = 3, la_num = 3, last_char = 0):
    if last_char == 1:
        s = (('la-'*la_num + '\n') * lines).rstrip('\n') + '!'
        return s
    else:
        s = (('la-' * la_num + '\n') * lines).rstrip('\n') + '.'
        return s

def new_song_generator(lines = 3, la_num = 3, last_char = 0):
    kuplet = ['la-']
    lines_list = []
    for i in range(lines):
        lines_list.append(''.join(kuplet*la_num))
    s = '\n'.join(lines_list)
    if last_char == 1:
        return s +'!'
    return s + '.'

print(new_song_generator(2,1,1))

