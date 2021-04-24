def ex2(symbol, data_list):
    for i in range(len(data_list)):
        if isinstance(data_list[i], int):
            smth = str(data_list[i]).replace(f'{symbol}', '')
            data_list[i] = int(smth) if smth != '' else None
        elif isinstance(data_list[i], str):
            data_list[i] = data_list[i].replace(f'{symbol}', '')
    return data_list


def macke_allowed(string):
    g = 0
    allowed = []
    dict_of_flags = {}
    for i in string:
        dict_of_flags[i] = False
    while g != len(string):
        for i in string[g:]:
            dict_of_flags[i] = True
            if False not in dict_of_flags.values():
                allowed.append(string[g:])
        g += 1
        for i in dict_of_flags.keys():
            dict_of_flags[i] = False
    return allowed


def macke_min_el(allowed):
    min_el = [allowed[0]]
    min_len = len(allowed[0])
    for el in allowed:
        if len(el) < min_len:
            min_el = [el]
            min_len = len(el)
        elif len(el) == min_len:
            min_el.append(el)
    return min_el


def ex1(string):
    allowed = macke_allowed(string)
    return macke_min_el(allowed)


print(ex2('1', [12, 1, 'abv', 'a1c3', '2031']))
print(ex1('12332214'))

