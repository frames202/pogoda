def n_p(item_list, g):
    while g != len(item_list):
        yield item_list[g]


def smth(item_list, g = 0, l = None):
    while True:
        l = n_p(item_list, g)
        for i in range(0, g):
            l.__next__
        flag = yield l.__next__

        if flag == 'next' and g != len(item_list)-1:
            g += 1
        elif flag == 'next' and g == len(item_list)-1:
            pass
        elif flag == 'previous' and g != 0:
            g -= 1
        elif flag == 'previous' and g == 0:
            g = 0

sc = smth(['1', '2', '3', '4', '5'])
print(next(sc))
print(next(sc))
