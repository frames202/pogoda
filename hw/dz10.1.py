a = [27, [3, 'a'], 7, [2, 5]]
b = []
g = 0

#1 rozpakovka listov
len_a = len(a)
while g <= len_a:
    if isinstance(a[g], list):
        b.extend(a[g])
    if a[g] is a[-1]:
        break
    g += 1

#2 proverka na chislo i suma
ans = 0
g = 0
while g < len(b):
    if not  str(b[g]).isdigit():
        g += 1
        continue
    for i in str(b[g]):
        ans += float(i)
        g += 1
print(f'{b}\n\n{ans}')
