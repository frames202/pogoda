a = int(input('height: '))
file = open('piramida.txt', 'w')

for i in range(0,a+1):
    file.write(' '*(a-i) + '*'*i*2+'*'+'\n')
file.close()
