a = '2 55 777 987 65 2 3 1 0 2 2'

i = 0
g = 0
s = 0
ans = ''

while i <= len(a):
    s = i
    g = i
    while a[g].isdigit():
        g += 1
    if a[s:g-1:].isdigit():
        ans += a[s:g-1:]
    i += g
print(ans)
