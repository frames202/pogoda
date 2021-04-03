def zapis(*args, **kwargs):
    args_in_file = ''
    kwargs_in_file = ''
    for i in args:
        args_in_file += f'{i}\n'
    for keys, values in kwargs.items():
        kwargs_in_file += f'{keys}: {values}\n'

    with open('parser.txt', 'w') as file:
        file.write(f'{args_in_file}{kwargs_in_file}')

    return None

def parser(file_name):
    args = []
    kwargs = {}
    with open(f'{file_name}', 'r') as file:
        file_lines = file.read()
        file_lines = file_lines.split('\n')

    for i in file_lines:
        if not ':' in i:
            args.append(i)
            continue
        for j in range(len(i)):
            if i[j] == ':':
                index = j
        kwargs[i[:index:]] = i[index+2:]

    return args, kwargs

print(zapis(1, 5, '6', 'a', '72', a = 'b', b = 17))
print(parser('parser.txt'))
