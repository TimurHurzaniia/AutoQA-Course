def pre_min(*args):
    res = sorted(args)
    return res[1]

print(pre_min(3,2,9,4,22,11))