g = 0
a = 115132219018763992565095597973971522401

while g <= 100:
    a_str = str(a)
    s = 0
    for i in range(len(a_str)):
        s += int(a_str[i])**len(a_str)
    if a == s:
        print(a)
        g += 1
    a += 1
