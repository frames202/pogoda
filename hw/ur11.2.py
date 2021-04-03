a = []
g = 0
l1 = [['видатний', 3], ['спадщина', 2], ['чия', 0], ['письменник,', 4], ['115', 1], ['томів.', None], ['науково-фантастичної', 5], ['пригодницької', 6]]               #list(input('input first str: '))
l2 =  [['творча', 1], ['великих', 5], ['налічує', 4], ['французький', 3], ['класик', 6], ['та', 7], ['літератури,', 2]]               #list(input('input second str: '))
t = True
a.append(l1[0][0])
elem = l1[0][1]
new_elem = None

while g <= len(l1)+len(l2):
    if t:
        list_ = l2
        t = False
    else:
        list_ = l1
        t = True
    a.append(list_[elem][0])
    elem = list_[elem][1]
    g += 1
    if elem is None:
        break

#2
ans = ''
for i in a:
    ans += i + ' '
print(ans)  
