a = float(input("input a: "))
b = float(input("input b: "))
c = float(input("input c: "))

d = b**2 - (4*a*c)

if a == 0:
    x = (c * -1) / b
    print(x)
elif d == 0:
    x = (b * -1)/(2 * a)
    print(x)
elif d > 0:
    x1 = ((b * -1)+(d ** 0.5))/(2 * a)
    x2 = ((b * -1)-(d ** 0.5))/(2 * a)
    print()
    print(x1)
    print(x2)
elif d < 0:
    print("There is no resolutions in this case!")
