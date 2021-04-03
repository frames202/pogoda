file = open('10-12344.txt', 'w')
for i in range(10, 12345):
    file.write(f'{i} ')
file.close()
