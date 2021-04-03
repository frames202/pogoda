t = input("input any text: ")
b = ""
l = ""
n = ""
g = 0 #

while g < len(t):
    if t[g].isalpha() == True:
        if t[g].islower() == True:
            l += t[g]
        elif t[g].isupper() == True:
            b += t[g]
    else:
        n += t[g]
    g += 1
print(b,"+", l,"+", n)
