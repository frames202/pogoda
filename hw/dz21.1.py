import random
def random10000_num():
    imena = ['valera', 'jenya', 'anton', 'tolya', 'dima', 'sergei', 'vlad', 'oleksandr', 'ivan', 'alex', 'inokentiy', 'terentiy']
    pr = ['zabolotniy', 'stilinski', 'chereshnya', 'vasilchenko', 'ostash', 'skripnik', 'redko', 'masenko', 'nestaiko', 'reznikov', 'pristaiko', 'fedorov']
    list_n = ['+38097', '+38096', '+38066', '+38099',  '+38093', '+38063']

    nomera = open('num_base.txt', 'w')
    for _ in range(0, 10000):
        nomer = random.choice(list_n)
        for _ in range(0, 7):
            nomer += str(random.randint(0, 9))
        nomera.write(f'{random.choice(imena)} {random.choice(pr)} {nomer}\n')
        
    nomera.close()
    return 'gotovo, file name: num_base.txt'


def ad_num(data):
    file_txt = open('num_base.txt', 'a')
    file_txt.write('\n'+data)
    return data


def find_num(data):
    file_txt = open('num_base.txt', 'r')
    file = file_txt.readlines()
    file_txt.close()
    index = None
    ans = []
    for i in range(len(file)):
        if data in file[i]:
            print('Nice')
            index = i
            ans.append(file[index][:-1])
    if index != None:
        return ans
    else:
        ans = 'No contact has been found.'
    return ans


def edit_num(data, new_num):
    file_txt = open('num_base.txt', 'r')
    file = file_txt.readlines()
    file_txt.close()
    for i in range(len(file)):
        if data in file[i]:
            print('Nice')
            index = i
            old_data = file[index][:-13]
            file.pop(index)
            file.insert(index, f'{old_data} {new_num}\n')
    file = ''.join(file)
    file_txt = open('num_base.txt', 'w')
    file_txt.write(file)
    file_txt.close()
    return [data, new_num]


def delete_num(data):
    file_txt = open('num_base.txt', 'r')
    file = file_txt.readlines()
    file_txt.close()
    index = None
    len_ = len(file)

    for i in range(0, len_):
        if data in file[i]:
            print('Nice')
            index = i
            file.pop(index)
            i -= 1
            len_ -= 1

    file = ''.join(file)
    file_txt = open('num_base.txt', 'w')
    file_txt.write(file)
    file_txt.close()
    return data

def same_num(data):
    file_txt = open('num_base.txt', 'r')
    file = file_txt.readlines()
    g = 0
    ans = False
    for i in file:
        if data in i:
            g += 1
        if g > 1:
            file_txt.close()
            ans = True
            return ans
    return ans

def most_num():
    file_txt = open('num_base.txt', 'r')
    file = file_txt.readlines()
    most = 0
    most_num = []
    for i in file:
        nomer = i[-14:-1]
        g = 0
        for j in file:
            if j[-14:-1] == nomer:
                g += 1
        if g > most:
            most_num = [nomer]
            most = g
        elif g == most:
            most_num.append(nomer)
    return [most_num, most] 
print(same_num('oleksandr fedorov'))
