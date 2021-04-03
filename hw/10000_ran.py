import random
def random10000_num()
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
