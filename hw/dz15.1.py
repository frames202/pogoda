import random as ran
a = []

for i in range(1,11):
    a.append(str(i))
for i in range(1,11):
    r = ran.choice(a)
    file = open(f'file{r}', 'w')
    a.remove(r)
    file.write(str(i))

#2
max = 0
for i in range(1,11):
    file = open(f'file{i}', 'r')
    file_str = file.read()
    if int(file_str) >= max:
        max = int(file_str)
        max_file = i
print(f'max is {max} in file{max_file}')
