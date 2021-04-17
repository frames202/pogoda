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


'''def big_pod(text):
	used = []
	longest = ''
	for i in range(len(text)):
		if text[i] not in used and text.count(text[i]) > 1:
			ind_1 = text.find(text[i])
			ind_2 = text.rfind(text[i])
			splited = text[ind_1: ind_2].split(text[i])
			for j in splited:
				longest = f'{text[i]}{j}{text[i]}' if len(j)+2 > len(longest) else longest
				used.append(text[i])

	return longest


print(big_pod('sdkjfhlazxnmcbzmnxbcmznxbcmznxbcae'))
print(big_pod('abcabeba'))
print(big_pod('aa'))'''


'''def big_pod_2(text):
	used = []
	longest = ''
	for i in range(len(text)):
		if text[i] not in used and text.count(text[i]) > 1:
			ind_1 = text.find(text[i])
			ind_2 = text.rfind(text[i])
			longest = text[ind_1: ind_2+1] if len(text[ind_1: ind_2+1]) > len(longest) else longest
			used.append(text[i])
	return longest

print(big_pod_2('sdakjfhlazxnmcbzmnxbcmznxbcmznxbcae'))
print(big_pod_2('abcabeba'))
print(big_pod_2('aa'))'''

'''def generate_hashtag(s):
    ans = s.split(' ')
    ans = '#' + ''.join([i.title() for i in ans]).replace(' ', '')
    print(ans)
    if len(ans) > 140 or ans == '#':
        return False
    else:
        return ans

print(generate_hashtag(''))
print(generate_hashtag('c i n'))'''


'''
def last_digit(n, kv):
	try:
		while True: 
			ans = (x for x in str(kv))
	except StopIteration:
		return ans
	return ans


print(last_digit(4, 1))#4
print(last_digit(4, 2))#6
print(last_digit(9, 7))#9
print(last_digit(10, 10 ** 10))#0
print(last_digit(2 ** 200, 2 ** 300))#6
print(last_digit(3715290469715693021198967285016729344580685479654510946723, 68819615221552997273737174557165657483427362207517952651))#7
'''

'''def flag_zero(number):
	for i in str(number)[1::]:
		if i != '0':
			return False
	return True

def is_interesting(number, awesome_phrases):
	print(number, awesome_phrases)
	going_uper = '1234567890'
	if number in awesome_phrases:
		print('awesome_phrases 1')
		return 2
	elif number+2 in awesome_phrases or number+1 in awesome_phrases:
		print('awesome_phrases 2')
		return 1

	if len(str(number)) >= 3 and str(number) == str(number)[::-1]:
		print('palindrom')
		return 2
	elif len(str(number)) >= 3 and flag_zero(number):
		print('flag_zero')
		return 2
	elif len(str(number)) >= 3 and str(number) in going_uper:
		print('groving')
		return 2
	elif len(str(number)) >= 3 and str(number) in going_uper[:9][::-1]+'0':
		print('shrinkig')
		return 2
	elif len(str(number+1)) >= 3 and str(number+1) in going_uper:
		print('close to groving 1')
		return 1
	elif len(str(number+2)) >= 3 and str(number+2) in going_uper:
		print('close to groving 2')
		return 1
	elif len(str(number+1)) >= 3 and str(number+1) in going_uper[:9][::-1]+'0':
		print('close to shrinkig 1')
		return 1
	elif len(str(number+2)) >= 3 and str(number+2) in going_uper[:9][::-1]+'0':
		print('close to shrinkig 2')
		return 1
	elif len(str(number+2)) >= 3 and flag_zero(number+2):
		print('close to flag_zero 2')
		return 1
	elif len(str(number+1)) >= 3 and flag_zero(number+1):
		print('close to flag_zero 1')
		return 1
	elif len(str(number+1)) >= 3 and str(number+1) == str(number+1)[::-1]:
		print('close to palindrom 1')
		return 1
	elif len(str(number+2)) >= 3 and str(number+2) == str(number+2)[::-1]:
		print('close to palindrom 2')
		return 1
	else:
		return 0



# "boring" numbers
print(is_interesting(3, [1337, 256]), '0')    # 0
print(is_interesting(3236, [1337, 256]), '0') # 0

# progress as we near an "interesting" number
print(is_interesting(11207, []), '0') # 0
print(is_interesting(11208, []), '0') # 0
print(is_interesting(11209, []), '1') # 1
print(is_interesting(11210, []), '1') # 1
print(is_interesting(11211, []), '2') # 2
# nearing a provided "awesome phrase"
print(is_interesting(1335, [1337, 256]), '1') # 1
print(is_interesting(1336, [1337, 256]), '1') # 1
print(is_interesting(1337, [1337, 256]), '2') # 2
'''


regex=""
def chek_pasw(smth, pasw):
    print(smth, pasw)
    flag_num = False
    flag_upper = False
    flag_lower = False
    for i in pasw:
        if i.isupper():
            flag_upper = True
        elif i.islower():
            flag_lower = True
        elif i.isdigit():
            flag_num = True
        elif not i.isdigit() and not i.isalpha():
            return False
    if len(pasw) >= 6 and flag_upper and flag_lower and flag_num:
        return True
    else:
        return False

print(chek_pasw(regex, 'fjd3IR9'), True)
print(chek_pasw(regex, 'ghdfj32'), False)
print(chek_pasw(regex, 'DSJKHD23'), False)
print(chek_pasw(regex, 'dsF43'), False)
print(chek_pasw(regex, '4fdg5Fj3'), True)
print(chek_pasw(regex, 'DHSJdhjsU'), False)
print(chek_pasw(regex, 'fjd3IR9.;'), False)
print(chek_pasw(regex, 'fjd3  IR9'), False)
print(chek_pasw(regex, 'djI38D55'), True)
print(chek_pasw(regex, 'a2.d412'), False)
print(chek_pasw(regex, 'JHD5FJ53'), False)
print(chek_pasw(regex, '!fdjn345'), False)
print(chek_pasw(regex, 'jfkdfj3j'), False)
print(chek_pasw(regex, '123'), False)
print(chek_pasw(regex, 'abc'), False)
print(chek_pasw(regex, '123abcABC'), True)
print(chek_pasw(regex, 'ABC123abc'), True)
print(chek_pasw(regex, 'Password123'), True)