'''def n_p(file, g):
    while g != len(file):
        yield file[g]


def smth(file_name, g = 0, l = None):
    file = open(f'{file_name}.txt', 'r')
    while True:
        l = n_p(file, g)
        for i in range(0, g):
            l.__next__()
        flag = yield l.__next__()

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
'''

def dz_1(list_of_strings):
    new_list_of_str = []
    while len(list_of_strings) != 0:
        min_len = len(list_of_strings[0])
        min_el = list_of_strings[0]
        for i in list_of_strings:
            if len(i) < min_len:
                min_el = i
                min_len = len(i)
        new_list_of_str.append(min_el)
        list_of_strings.remove(min_el)

    return new_list_of_str


def dz_2(num):
    ans = 0
    while num % 2 == 0:
        num = num / 2
        ans += 1
    return ans

def dz_3(string):
    ans = [0]
    ans = [ans[-1] + int(i) for i in string if i.isdigit()]
    return sum(ans)


print(dz_1(['a', 'bca', 'as']))
print(dz_2(9))
print(dz_2(8))
print(dz_3('a2sd15sd4g4g')) #16
