import random as ran

def ran_dict(min = 1, max = 1000):
	new_dict = {}
	while len(new_dict) < 100:
		ran_num = ran.randint(min, max)
		if ran_num not in new_dict.keys():
			new_dict[ran_num] = ran_num ** 2
		else:
			continue

	return new_dict

def sort_keys(not_sorted):
	keys_in_dict = []
	sorted_dict = {}
	for key in not_sorted.keys():
		keys_in_dict.append(key)

	keys_in_dict = sorted(keys_in_dict)
	for key in keys_in_dict:
		sorted_dict[key] = not_sorted[key]

	return sorted_dict


a = ran_dict()
print(a)
print(sort_keys(a))
