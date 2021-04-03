#1
ans = []

for i in range(2,202,2):
    ans.append(i)
print(ans)

#2
for i in range(0,80,1):
    if str(ans[i])[-1] == '2':
        ans.pop(i)
print(ans)

#3
for i in range(len(ans)-2):
    str(ans[i]).split('0')
    str(ans[i]).join(str(ans[i+1]))
print(ans)
