f = open('first1.txt', 'r')
s = open('second1.txt', 'r')
ans = open('answer.txt', 'w')

f = f.readlines()
s = s.readlines()

for i in range(len(f)):
    if i+1 >= len(f):
        break
    f1 = f[i].strip()
    s1 = s[i].strip()
    if f1 == '':
        f1 = 0
    else:
        f1 = int(f1)
    if s1 == '':
        s1 = 0
    else:
        s1 = int(s1)
    ans.write(f'{f1}       {s1}       =>   {f1+s1}\n')
