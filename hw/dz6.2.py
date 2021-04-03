a = 'abc Dima 123'
i = 0
s = 0
g = 0
ans = ''

while i <= len(a):
    s = i
    g = i
    if a[i].isalpha() or a[i].isdigit():
        while a[g].isalpha() or a[g].isdigit():
            g += 1
            if g == len(a):
                break
        p = a[s:g:]
        ans += p[::-1]
    i += g-1
print(ans)
