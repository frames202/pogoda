import random as ran
def ran_nechet(begin, end):
    a = ran.randint(begin, end)
    if a % 2 == 0:
        a += 1
    return a

def how_much(begin, end):
    c = []
    b = 0

    if begin % 2 == 0:
        begin += 1
        b += 1
    else:
        b = begin

    while b < end:
        c.append(b)
        b += 2
        print(c)
    b = 0
    ans = 0
    lists = []
    g = 0

    while lists != c:
        b = ran_nechet(begin, end)
        lists.append(b)
        print(b)
        print(lists)
        if lists[g] == c[g]:
            g += 1
            continue
        else:
            lists = []
            g = 0
        ans += 1


    return ans

print(how_much(0, 7))
