def n_p(file, g):
    while g != len(file):
        yield file[g]


def smth(file_name, g = 0, l = None):
    file = open(f'{file_name}.txt', 'r')
    while True:
        l = n_p(file, g)
        for i in range(0, g):
            l.__next__
        flag = yield l.__next__

        if flag == 'next' and g != len(file)-1:
            g += 1
        elif flag == 'next' and g == len(file)-1:
            pass
        elif flag == 'previous' and g != 0:
            g -= 1
        elif flag == 'previous' and g == 0:
            g = 0

sc = smth('ex1')
print(next(sc))
print(next(sc))
