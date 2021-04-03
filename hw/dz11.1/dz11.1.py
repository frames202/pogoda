file = None
for i in range(1,11):
    file = open(f'{i}.txt', 'w')
    file.write(str(i))
    file.close()
