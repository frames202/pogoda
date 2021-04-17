while True:
	print('if u want to stop, input "b" into all spaces.')
	n1 = input('first num:\n')
	n2 = input('second num:\n')
	act= input('action:\n')


	try:
		if act == 'b' and n1 == 'b' and n2 == 'b':
			break
		elif act == '*':
			print('\n', int(n1) * int(n2)) 
		elif act == '/':
			print('\n', int(n1) / int(n2)) 
		elif act == '-':
			print('\n', int(n1) - int(n2))
		elif act == '+':
			print('\n', int(n1) + int(n2))
		elif act == '**':
			print('\n', int(n1) ** int(n2))
		elif act == '//':
			print('\n', int(n1) // int(n2))
		elif act == '%':
			print('\n', int(n1) % int(n2))
		else:
			raise ValueError('check your input and try again.')
	except: 
		print('check your input, and try again.')


	'''	actions = ['*', '/', '-', '+', '**', '//', '%']
	ex = input('Input your exsample (only one action: *, /, -, +, **, //, %):\n')
	g = 0
	act = []
	for i in actions:
		if i in ex and len(act) == 0:
			act.append(g)
		elif i in ex and len(act) != 0:
			raise ValueError('You can input only one action!')
		elif i not in ex:
			g += 1

	data = ex.split(actions[act])
	if len(data) > 2:
		raise ValueError('You can input only two nums!')
	
	print(data, g, act)

		if g == 0:
			print(int(data[0]) * int(data[1])) 
		elif g == 1:
			print(int(data[0]) / int(data[1])) 
		elif g == 2:
			print(int(data[0]) - int(data[1]))
		elif g == 3:
			print(int(data[0]) + int(data[1]))
		elif g == 4:
			print(int(data[0]) ** int(data[1]))
		elif g == 5:
			print(int(data[0]) // int(data[1]))
		elif g == 6:
			print(int(data[0]) % int(data[1]))
				'''

