def to0(digit):
    if digit == 0:
        print(digit)
        return 0

    if digit > 0:
        print(digit)
        return digit + to0((digit*-1)+1)
    else:
        print(digit)
        return digit + to0((digit*-1)-1)


print(to0(-7))
