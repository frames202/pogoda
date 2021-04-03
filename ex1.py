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


'''def gen(name_list, i = 0):
	while i != len(name_list)-1:
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
'''


'''\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\'''


def big_pod(text):
	used = []
	longest = ''
	for i in range(len(text)):
		if text[i] not in used and text.count(text[i]) > 1:
			if text[0] == text[i] and text[-1] == text[i]:
				f = 2
			elif text[0] == text[i] and text[-1] != text[i]:
				f = 0
			elif text[0] != text[i] and text[-1] == text[i]:
				f = -1
			elif text[0] != text[i] and text[-1] != text[i]:
				f = None
		else:
			continue

		if f == 2:
			splited = text.split(text[i])
			for j in splited:
				longest = f'{text[i]}{j}{text[i]}' if len(j)+2 > len(longest) else longest
				used.append(text[i])
		elif f == 0:
			splited = text.split(text[i])
			splited.pop(-1)
			for j in splited:
				longest = f'{text[i]}{j}{text[i]}' if len(j)+2 > len(longest) else longest
				used.append(text[i])
		elif f == -1:
			splited = text.split(text[i])
			splited.pop(0)
			for j in splited:
				longest = f'{text[i]}{j}{text[i]}' if len(j)+2 > len(longest) else longest
				used.append(text[i])
		elif f == None:
			splited = text.split(text[i])
			splited.pop(0)
			splited.pop(-1)
			for j in splited:
				longest = f'{text[i]}{j}{text[i]}' if len(j)+2 > len(longest) else longest
				used.append(text[i])

	return longest

print(big_pod('sdkjfhlazxnmcbzmnxbcmznxbcmznxbcae'))
print(big_pod('abcabeba'))
