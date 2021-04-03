f = open('first.txt', 'r')
s = open('second.txt', 'r')
b = ''
fl = []
sl = []

#1
f = f.read()
s = s.read()
f += ' '
s += ' '

for i in range(len(f)):
    if f[i].isdigit():
        b += f[i]
    if f[i].isdigit() and not f[i+1].isdigit():
        fl.append(int(b))
        b = ''
for i in range(len(s)):
    if s[i].isdigit():
        b += s[i]
    if s[i].isdigit() and not s[i+1].isdigit():
        sl.append(int(b))
        b = ''

#2
if len(fl)>len(sl):
    sl.append(0)
elif len(sl)>len(fl):
    fl.append(0)

#3
file  = open('answer.txt', 'w')
for i in range(len(fl)):
    file.write(f'{sl[i]} + {fl[i]} => {sl[i] + fl[i]}\n')
