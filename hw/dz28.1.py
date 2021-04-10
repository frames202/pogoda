'''import random as ran

def ran_1000():
	ans = []
	for _ in range(0, 1000):
		ans.append(ran.randint(0, 1000000))

	return ans


def filter(not_filtered_list):
	filtered_list = []
	for item in not_filtered_list:
		if (item%10 + item%100//10) % 2 == 0:
			filtered_list.append(item)

	return filtered_list


def smth(not_remaked):
	remaked = []
	for item in not_remaked:
		remaked.append([item%10, item%100//10])

	return remaked


print(smth(filter(ran_1000())))'''

'''\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\'''

def gen(name_list, i = 0):
	while i != len(name_list):
		flag = yield name_list[i]
		while flag == 'nextone':
			i += 1
			flag = yield name_list[i]



func = gen(['a', 'b', 'c', 'd', 'e'])
print(func.__next__())
print(func.__next__())
print(func.__next__())
print(func.send('nextone'))
print(func.__next__())
print(func.send('nextone'))
print(func.send('nextone'))
print(func.send('nextone'))
print(func.__next__())
print(func.send('nextone'))
