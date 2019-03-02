def pre_min(*args):
    res = sorted(args)
    i = 1
    while res[i] == res[0]:
        i += 1
    return res[i]

print(pre_min(3,2,1,1,9,4,22,11))