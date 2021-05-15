import requests
import pprint
import random as ran
import json
from colorama import init, Fore, Back, Style
init()


city = 'Kiev' #city
API_KEY = 'd8f1728f479da18a52e428f97e8aac71' #open weather API-Key
hours = {'00': 0, '03': 1, '06': 2, '09': 3, '12': 4, '15': 5, '18': 6, '21': 7} #all avaible times using 5-days sub
descriptions_advises_2 = {'200,201,202': [], '210,211,212,221': [], '230,231,232': []}
descriptions_advises_3 = {'300,301,302': [], '310,311,312': [], '313,314': [], '321': []}
descriptions_advises_5 = {'500,501,502,503,504': [], '511': [], '520,521,522,531': []}
descriptions_advises_6 = {'600,601,602': [], '611': [], '612,613': [], '615,616': [], '620,621,622': []}
descriptions_advises_7 = {'701': [], '711': [], '721': [], '731': [], '741': [], '751': [], '761': [], '762': [], '771': [], '781': []}
descriptions_advises_8 = {'800': [], '801': [], '802,803': [], '804': []}

response = requests.get(f'https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric') #getting info
response = response.json() #making JSON
hour_now = hours[response['list'][0]['dt_txt'][11:13]] #what's hour now
day_now = response['list'][0]['dt_txt'][5:10] #now we dont need it
all_info = {0: {0: None, 1: None, 2: None, 3: None, 4: None, 5: None, 6: None}} #info for all avaible times for our 5 days


#func that searches a random advice for our weather
def search_advice(weather_id, descriptions_advices = json.dumps(open('descriptions_advices.json', 'r').read())):
	for i in descriptions_advices.keys():
			if str(weather_id) in i:
				key = i
	return f'\n{ran.choice(descriptions_advices[key])}'


for i in range(len(response['list'][0:7-hour_now+1])): #making first day's weather dict
	weather_now = response['list'][i]['main']
	t_now = weather_now['temp']
	min_t_now = weather_now['temp_min']
	max_t_now = weather_now['temp_max']
	humidity_now = weather_now['humidity']
	description_now = response['list'][i]['weather'][0]['description']
	id_now = response['list'][i]['weather'][0]['id']

	all_info[0][int(hours[response['list'][i]['dt_txt'][11:13]])] = f"in {response['list'][i]['dt_txt'][11:13]}-{int(response['list'][i]['dt_txt'][11:13])+3} temperature is {min_t_now} - {max_t_now}\nhumidity = {humidity_now}%\n({id_now}) {description_now}\n\t{search_advice(id_now)}\n\t\t{response['list'][i]['dt_txt'][:-6]}-{int(response['list'][i]['dt_txt'][-8:-6])+3}{response['list'][i]['dt_txt'][-6:]}"


response['list'] = response['list'][8-hour_now::] #deleting parsed info
g = 0
for i in range(1, 5): #making other day's weather dict
	all_info[i] = {}
	for j in range(0, 8):
		k = (i-1)*7+j
		weather_now = response['list'][k]['main']
		t_now = weather_now['temp']
		min_t_now = weather_now['temp_min']
		max_t_now = weather_now['temp_max']
		humidity_now = weather_now['humidity']
		description_now = response['list'][k]['weather'][0]['description']
		id_now = response['list'][k]['weather'][0]['id']

		all_info[i][hours[response['list'][k]['dt_txt'][11:13]]] = f"in {response['list'][k]['dt_txt'][11:13]}-{int(response['list'][k]['dt_txt'][11:13])+3} temperature is {min_t_now} - {max_t_now}\nhumidity = {humidity_now}%\n({id_now}) {description_now}\n\t{search_advice(id_now)}\n\t\t{response['list'][k]['dt_txt'][:-6]}-{int(response['list'][k]['dt_txt'][-8:-6])+3}{response['list'][k]['dt_txt'][-6:]}"

day = 0
hour = hour_now

while True:
	print(Back.YELLOW + Fore.GREEN + Style.BRIGHT + all_info[day][hour])
	print(Style.RESET_ALL)
	print(Back.WHITE + Fore.BLUE)
	call = input(f'"<" - next day | chose time(0-7) | previous day - ">"\n\t\t"break" to stop executing\t\n')
	print(Style.RESET_ALL)
	if call == '<' and day != 0 and all_info[day-1][hour] != None:
		day -= 1
	elif call == '>' and day != 4 and all_info[day+1][hour] != None:
		day += 1
	elif len(call) == 1 and call.isdigit():
		if int(call) >= 0 and int(call) <= 7:
			if all_info[day][int(call)] != None:
				hour = int(call)
			else:
				print(Back.RED + Fore.BLACK + "Time isn't correct!")
				print(Style.RESET_ALL)
		else:
			print(Back.RED + Fore.BLACK + "Time isn't correct!")
			print(Style.RESET_ALL)
	elif call == '<':
		print(Back.RED + Fore.BLACK + "It's the first day!")
		print(Style.RESET_ALL)
	elif call == '>':
		print(Back.RED + Fore.BLACK + "It's the last day!")
		print(Style.RESET_ALL)
	elif call == 'break':
		break
	else:
		print(Back.RED + Fore.BLACK + "Check your input, it isn't correct!")
		print(Style.RESET_ALL)

