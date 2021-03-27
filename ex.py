'''from colorama import init, Fore, Style,Back 					#colorama

a = ''
init(convert = True)

while a != '0':
	a = input('chose a color:\nRed-1\nBlue-2\nGreen-3\nWhite-4\nPurple-5\nBlack-6\nYellow-7\nprint 0 to end: \n')
	text = input('Input text here: ')
	if a == '1':
		print(Fore.RED + Style.BRIGHT + text + '\n' + Style.RESET_ALL)		

	elif a == '2':
		print(Fore.BLUE + Style.BRIGHT + text + '\n' + Style.RESET_ALL)
		

	elif a == '3':
		print(Fore.GREEN + Style.BRIGHT + text + '\n' + Style.RESET_ALL)
		

	elif a == '4':
		print(Fore.WHITE + Style.BRIGHT + text + '\n' + Style.RESET_ALL)
		

	elif a == '5':
		print(Fore.MAGENTA + Style.BRIGHT + text + '\n' + Style.RESET_ALL)
		

	elif a == '6':
		print(Fore.BLACK + Back.WHITE + text + '\n' + Style.RESET_ALL)
		

	elif a == '7':
		print(Fore.YELLOW + Style.BRIGHT + text + '\n' + Style.RESET_ALL)
		
'''

'''from PIL import Image					#PIL
f = Image.open("ex.png").show() 

'''

'''nothing to add'''


