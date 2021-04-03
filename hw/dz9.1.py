#1
import random as ran
lis = []

while len(lis) <= 100:
    a = str(float(str(f'{ran.randint(150,299)}.{ran.randint(0,9)}')))
    if not a in lis:
        lis.append(a)

#2
lis.sort()
g = 0
ans = 0

for i in range(0, 101): 
    while g <= 3:
        if lis[i][g] == '.':
            g += 1
            ans += float(lis[i][g])/10
            continue
        ans += float((lis[i][g]))
        g += 1
    g = 0

#1*
while True:
    print("print:\n1-if you want to see answer.\n2-to see list with random nums.\n3-to see answer and list.\n")
    inp = input('input your chois: ')
    if inp == '1':
        print(f'\n{ans}')
    elif inp == '2':
        print(f'\n{lis}')
    elif inp == '3':
        print(f'\n{ans}\n{lis}')
    break
