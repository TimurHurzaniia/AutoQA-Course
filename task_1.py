def song_generator(lines = 3, la_num = 3, last_char = 0):
    if last_char == 1:
        s = (('la-'*la_num + '\n') * lines).rstrip('\n') + '!'
        return s
    else:
        s = (('la-' * la_num + '\n') * lines).rstrip('\n') + '.'
        return s

print(song_generator(2,2,1))