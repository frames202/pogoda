import random as ran

places = {1: '_', 2: '_', 3: '_', 4: '_', 5: '_', 6: '_', 7: '_', 8: '_', 9: '_'}
f = True
b = True


def print_field(places):
    field_f_print = f" _ _ _ \n|{places['1']}|{places['2']}|{places['3']}|\n|{places['4']}|{places['5']}|{places['6']}|\n|{places['7']}|{places['8']}|{places['9']}|"

    return field_f_print


def make_move(icon, cell_num):
    if places[cell_num] != '_':
        return [places, False]
    else:
        places[cell_num] = icon
        return [places, True]


def play_again():
    ask = input('do u want to play again?\nif yes input "1"\n if no: "2"')
    if ask == '1':
        return [{1: '_', 2: '_', 3: '_', 4: '_', 5: '_', 6: '_', 7: '_', 8: '_', 9: '_'}, True]
    else:
        return ['break']


while True:
    bot = True if input('if u wanna to turn on the bot, print"1"\n else: "2"\n') == 2 else False
    if b == True:
        pass
    else:
        break
    if bot == False:
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
                print(f"{places[5]}'s wins!")
                ask_to_play = play_again()
                if len(ask_to_play) > 1:
                    places = ask_to_play[0]
                    f = ask_to_play[1]
                    b = True
                    break
                else:
                    b = True
                    break
            elif places[1] == places[2] == places[3] or places[3] == places[6] == places[9] and places[3] != '_':
                print(f"{places['3']}'s wins!")
                ask_to_play = play_again()
                if len(ask_to_play) > 1:
                    places = ask_to_play[0]
                    f = ask_to_play[1]
                    b = True
                    break
                else:
                    b = True
                    break
            elif places[1] == places[4] == places[7] or places[7] == places[8] == places[9] and places[7] != '_':
                print(f"{places['7']}'s wins!")
                ask_to_play = play_again()
                if len(ask_to_play) > 1:
                    places = ask_to_play[0]
                    f = ask_to_play[1]
                    b = True
                    break
                else:
                    b = True
                    break
            elif places[1] == places[2] == places[3] == places[4] == places[5] == places[6] == places[7] == places[8] == places[9]:
                print(f'noone win, drow!')
                ask_to_play = play_again()
                if len(ask_to_play) > 1:
                    places = ask_to_play[0]
                    f = ask_to_play[1]
                    b = True
                    break
                else:
                    b = True
                    break
            else:
                pass

    else:
        while True:
            cell_num = input('input cell numer:\n')
            if f == True:
                places_n_flag = make_move('x', cell_num)
                f = False
            else:
                r = ran.randint(1, 9)
                places_n_flag = make_move('o', r) if places[r] == '_' else None
                f = True

            if places_n_flag[1] == True:
                print(print_field(places_n_flag[0]))
            else:
                print('This place is claimed, try again!')
                continue

            if places[1] == places[5] == places[9] or places[3] == places[5] == places[7] and places[5] != '_':
                print(f"{places['5']}'s wins!")
                ask_to_play = play_again()
                if len(ask_to_play) > 1:
                    places = ask_to_play[0]
                    f = ask_to_play[1]
                    b = True
                    break
                else:
                    b = True
                    break
            elif places[1] == places[2] == places[3] or places[3] == places[6] == places[9] and places[3] != '_':
                print(f"{places['3']}'s wins!")
                ask_to_play = play_again()
                if len(ask_to_play) > 1:
                    places = ask_to_play[0]
                    f = ask_to_play[1]
                    b = True
                    break
                else:
                    b = True
                    break
            elif places[1] == places[4] == places[7] or places[7] == places[8] == places[9] and places[7] != '_':
                print(f"{places['7']}'s wins!")
                ask_to_play = play_again()
                if len(ask_to_play) > 1:
                    places = ask_to_play[0]
                    f = ask_to_play[1]
                    b = True
                    break
                else:
                    b = True
                    break
            elif places[1] == places[2] == places[3] == places[4] == places[5] == places[6] == places[7] == places[8] == places[9]:
                print(f'noone win, drow!')
                ask_to_play = play_again()
                if len(ask_to_play) > 1:
                    places = ask_to_play[0]
                    f = ask_to_play[1]
                    b = True
                    break
                else:
                    b = False
                    break
            else:
                pass
