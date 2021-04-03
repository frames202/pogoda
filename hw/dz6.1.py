a = '2 -5 99 -8 56 -333 5'

i = 0
ans = 0
g = 0
s = None

while i <= len(a):
    s = i
    g = i
    if a[i].isdigit():
        while a[g].isdigit():
            g += 1
        if a[s-1] == '-':
            ans -= int(a[s:g:])
        elif a[s:g-1:].isdigit():
            ans += int(a[s:g:])
        print(ans)
    i += g
    
print(ans)
# ans = -184
