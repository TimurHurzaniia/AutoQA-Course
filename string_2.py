def verbing(s):
    if len(s) >= 3:
        if s[-3::] == 'ing':
            new_s = s + 'ly'
            return new_s
        new_s = s + 'ing'
        return new_s
    else:
        return s

def not_bad(s):
    not_index = s.find('not')
    bad_index = s.find('bad')
    if bad_index > not_index:
        new_s = s[:not_index] + 'good' + s[bad_index+3:]
        return new_s
    return s

def front_back(a, b):
    if len(a)%2 != 0:
        res1 = '{}'.format(a[:(len(a)//2)+1])
        res2 = '{}'.format(a[(len(a)//2)+1:])
    else:
        res1 = '{}'.format(a[:(len(a)//2)])
        res2 = '{}'.format(a[(len(a)//2):])
    if len(b)%2 != 0:
        res3 = '{}'.format(b[:(len(b)//2)+1])
        res4 = '{}'.format(b[(len(b)//2)+1:])
    else:
        res3 = '{}'.format(b[:(len(b)//2)])
        res4 = '{}'.format(b[(len(b)//2):])
    return '{}{}{}{}'.format(res1, res3, res2, res4)


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{}got: {} expected: {}'.format(prefix, repr(got), repr(expected)))

def main():
    print('verbing')
    test(verbing('hail'), 'hailing')
    test(verbing('swiming'), 'swimingly')
    test(verbing('do'), 'do')


    print('\nnot_bad')
    test(not_bad('This movie is not so bad'), 'This movie is good')
    test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
    test(not_bad('This tea is not hot'), 'This tea is not hot')
    test(not_bad("It's bad yet not"), "It's bad yet not")


    print('\nfront_back')
    test(front_back('abcd', 'xy'), 'abxcdy')
    test(front_back('abcde', 'xyz'), 'abcxydez')
    test(front_back('Kitten', 'Donut'), 'KitDontenut')

if __name__ == '__main__':
    main()
