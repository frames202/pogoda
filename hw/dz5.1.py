g = 0
h = -1
j = 0
f = 10

while j <= 100:
    if len(str(f)) % 2 == 0:
        while g != len(str(f)):
            if str(f)[g] == str(f)[h]:
                a = 1
                g += 1
                h -= 1
            elif str(f)[g] != str(f)[h]:
                a = 0
            
            if a == 1:
                j += 1
                print(f)
                print(j)
                f += 1
                g = 0
                h = -1
                a = 0
            else:
                f += 1
                g = 0
                h = -1
                a = 0
            

        
    if len(str(f)) % 2 == 1:
        while g != len(str(f))-2:
            if str(f)[g] == str(f)[h]:
                a = 1
                g += 1
                h -= 1
            elif str(f)[g] != str(f)[h]:
                a = 0
            
            if a == 1:
                j += 1
                print(f)
                print(j)
                f += 1
                g = 0
                h = -1
                a = 0
            else:
                f += 1
                g = 0
                h = -1
                a = 0
            if j > 100:
                break
