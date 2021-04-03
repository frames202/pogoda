import random

data_input = input('Text here: ')
data_list = data_input.split()
elems_in_second = len(data_list) // 2
elems_in_first = len(data_list) - elems_in_second

first = []
second = []
places_first = []
places_second = []
for i in range(elems_in_first):
    first.append([])
    places_first.append(i)
for i in range(elems_in_second):
    second.append([])
    places_second.append(i)

first[0].append(data_list[0])
next_index = random.choice(places_second)
places_second.remove(next_index)
places_first.remove(0)
first[0].append(next_index)
next_list_index = 2


is_first = True
for word in data_list[1:]:
    if next_list_index % 2 == 0:
        next_place_list = places_first
        next_list = second
    else:
        next_place_list = places_second
        next_list = first

    if not next_place_list:
        new_next_index = None
        next_list[next_index].append(word)
        next_list[next_index].append(new_next_index)
        break

    new_next_index = random.choice(next_place_list)
    next_place_list.remove(new_next_index)
    next_list[next_index].append(word)
    next_list[next_index].append(new_next_index)
    next_index = new_next_index

    next_list_index += 1
print(first, '\n', second)
