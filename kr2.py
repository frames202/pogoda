def z1(a):
	a = ' '.join(a)
	a = a.split(' ')
	a.reverse()
	return ''.join(a)

def z2(a1 = 11, a2 = 127):
	if a1 <= 127:
		yield a1
		a1 += 1
		z = z2(a1, a2)
		yield next(z)


def z3(num):
	num = [int(i) for i in str(num)]
	list_bools = []
	for i in range(len(num)):**
		if num[i] % num[i-1] == 0 and i != 0:
			list_bools.append(True)
		else:
			list_bools.append(False)
	return list_bools

def z4(num1, num2):
	for i in range(num1, num2):
		yield i


def task6(num = 10000):
    ans = 0
    for i in range(2, num+1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            ans+=1
    return ans


print(task6(10000))


print(z1('123'))
print(z3(73312))
gen = z2()
gen2 = z4(1, 10)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen2))
print(next(gen2))
print(next(gen2))
print(z6(10000))


def macke_allowed(string):
    g = 0
    allowed = []
    dict_of_flags = {}
    for i in string:
        dict_of_flags[i] = False
    while g != len(string):
        for i in string[g:]:
            dict_of_flags[i] = True
            if False not in dict_of_flags.values():
                allowed.append(string[g:])
        g += 1
        for i in dict_of_flags.keys():
            dict_of_flags[i] = False
    return allowed


def macke_min_el(allowed):
    min_el = [allowed[0]]
    min_len = len(allowed[0])
    for el in allowed:
        if len(el) < min_len:
            min_el = [el]
            min_len = len(el)
        elif len(el) == min_len:
            min_el.append(el)
    return min_el


def ex1(text):
	top = []
	counts = {}
	text = text.split(' ')
	text.remove('')
	for i in text:
		counts[text.count(i)] = {i}
	top.append(counts[max(counts.keys())])
	del counts[max(counts.keys())]
	top.append(counts[max(counts.keys())])
	del counts[max(counts.keys())]
	top.append(counts[max(counts.keys())])
    allowed = macke_allowed(top)
    return macke_min_el(allowed)


def v5(str):
	top = []
	counts = {}
	text = text.split(' ')
	text.remove('')
	for i in text:
		counts[text.count(i)] = {i}
	top.append(counts[max(counts.keys())])
	del counts[max(counts.keys())]
	top.append(counts[max(counts.keys())])
	del counts[max(counts.keys())]
	top.append(counts[max(counts.keys())])


print(v5('aabec'))