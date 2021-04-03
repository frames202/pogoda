t = input("input any text: ")
g = 0 #Счетчик
b = ""

while g < len(t):
    if t[g].isupper == True:
        b[-g-1] = t[g]
        g += 1
        print("upper")
    else:
        print("leter, num")
        b[g] = t[g]
        g += 1
print(b)
