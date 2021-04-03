def check_way(way):
    horizon = 0
    vertical = 0
    if len(way) != 10:
        return False
    for i in way:
        if i == 'w':
            horizon -= 1
        elif i == 's':
            vertical -= 1
        elif i == 'e':
            horizon += 1
        elif i == 'n':
            vertical += 1
    if horizon == 0 and vertical == 0:
        return True
    else:
        return False

print(check_way(['n', 'n', 'w', 'e', 'n', 'e', 's', 's', 'w', 's']))
