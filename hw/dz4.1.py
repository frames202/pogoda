t = input("input any text: ")
g = 0
ans = ""

while g < len(t):
    if t[g].isdigit() == True:
        ans += t[g]
        if t[g+1].isalpha() == True:
            ans += t[g + 1].upper()
            g += 2
        else:
            g += 1
        print("num")
    else:
        ans += t[g]
        print("later")
        g += 1
print(ans)
