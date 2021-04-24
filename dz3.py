def z3(l, not_accesable = '1'):
	for i in range(len(l)):
		if isinstance(l[i], list):
			l[i] = z3(l[i])
		elif isinstance(l[i], str):
			l[i] = l[i].replace(not_accesable, '')
		elif isinstance(l[i], float):
			l[i] = float(str(l[i]).replace(not_accesable, ''))
		elif isinstance(l[i], int):
			l[i] = int(str(l[i]).replace(not_accesable, ''))
	return l


print(z3([123, 321, '31', '676767767189898',[123,[[12], '12']]]))