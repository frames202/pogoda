places = {'1': '_', '2': '_', '3': '_', '4': '_', '5': '_', '6': '_', '7': '_', '8': '_', '9': '_'}
f = True


def print_field(places):
    field_f_print = f" _ _ _ \n|{places['1']}|{places['2']}|{places['3']}|\n|{places['4']}|{places['5']}|{places['6']}|\n|{places['7']}|{places['8']}|{places['9']}|"

    return field_f_print


def make_move(icon, cell_num):
    if places[cell_num] != '_':
        return [places, False]
    else:
        places[cell_num] = icon
        return [places, True]


while True:
    cell_num = input('input cell numer:\n')
    if f == True:
        places_n_flag = make_move('x', cell_num)
        f = False
    else:
        places_n_flag = make_move('o', cell_num)
        f = True

    if places_n_flag[1] == True:
        print(print_field(places_n_flag[0]))
    else:
        print('This place is claimed, try again!')
        continue

    if places[1] == places[5] == places[9] or places[3] == places[5] == places[7] and places[5] != '_':
        print(f"{places['5']}'s wins!")
        break
    elif places[1] == places[2] == places[3] or places[3] == places[6] == places[9] and places[3] != '_':
        print(f"{places['3']}'s wins!")
        break
    elif places[1] == places[4] == places[7] or places[7] == places[8] == places[9] and places[7] != '_':
        print(f"{places['7']}'s wins!")
        break
    else:
        pass
