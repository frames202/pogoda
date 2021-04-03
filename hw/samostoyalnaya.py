#1
for i in range(10,10000):
    if str(i) == str(i)[::-1]:
        print(i)
#2
a = '12b31j21j23j12hbj1k123'
g = 0
for i in a:
    if i.isdigit():
        g += int(i)
print(g)
#3
b = []
a = []
ans = 0
for i in range(12,12346):
    a.append(i)
for i in a:
    if i%17 == 0 and i%8 == 0:
        b.append(i)
for i in b:
    i_str = str(i)
    ans += i_str.count('0')
print(ans)
#4
a = ''
b = ''
ans = 0
for i in a:
    if i.isdigit():
        b+=i
    ans += int(b)
    b = ''
print(ans)

#5
