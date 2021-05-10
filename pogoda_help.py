import requests
import pprint
from colorama import Fore, Back, Style

city = 'Kiev' #city
API_KEY = 'd8f1728f479da18a52e428f97e8aac71' #open weather API-Key
hours = {'00': 0, '03': 1, '06': 2, '09': 3, '12': 4, '15': 5, '18': 6, '21': 7} #all avaible times using 5-days sub

response = requests.get(f'https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric') #getting info
response = response.json() #making JSON
hour_now = hours[response['list'][0]['dt_txt'][11:13]] #what's hour now
day_now = response['list'][0]['dt_txt'][5:10] #now we dont need it
all_info = {0: {0: None, 1: None, 2: None, 3: None, 4: None, 5: None, 6: None}} #info for all avaible times for our 5 days


for i in range(len(response['list'][0:7-hour_now+1])): #making first day's weather dict
	weather_now = response['list'][i]['main']
	t_now = weather_now['temp']
	min_t_now = weather_now['temp_min']
	max_t_now = weather_now['temp_max']
	humidity_now = weather_now['humidity']
	description_now = response['list'][i]['weather'][0]['description']

	all_info[0][int(hours[response['list'][i]['dt_txt'][11:13]])] = f"in {response['list'][i]['dt_txt'][11:13]}-{int(response['list'][i]['dt_txt'][11:13])+3} temperature is {min_t_now} - {max_t_now}\nhumidity = {humidity_now}%\n{description_now}\n\t\t{response['list'][i]['dt_txt'][:-6]}-{int(response['list'][i]['dt_txt'][-8:-6])+3}{response['list'][i]['dt_txt'][-6:]}"


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
		all_info[i][hours[response['list'][k]['dt_txt'][11:13]]] = f"in {response['list'][k]['dt_txt'][11:13]}-{int(response['list'][k]['dt_txt'][11:13])+3} temperature is {min_t_now} - {max_t_now}\nhumidity = {humidity_now}%\n{description_now} \n\t\t{response['list'][k]['dt_txt'][:-6]}-{int(response['list'][k]['dt_txt'][-8:-6])+3}{response['list'][k]['dt_txt'][-6:]}"

day = 0
hour = hour_now

while True:
	print(Back.YELLOW + Fore.GREEN + all_info[day][hour] + Style.RESET_ALL)
	call = input(f'{Back.WHITE}{Fore.BLUE}"<" - next day | chose time(0-7) | previous day - ">"\n\t\t"break" to stop executing{Style.RESET_ALL}')
	if call == '<' and day != 0:
		day -= 1
	elif call == '>' and day != 4:
		day += 1
	elif len(call) == 1 and call.isdigit():
		if int(call) >= 0 and int(call) <= 7:
			hour = int(call)
		else:
			print(Back.RED + Fore.BLACK + "Time isn't correct!" + Style.RESET_ALL)
	elif call == '<':
		print(Back.RED + Fore.Black + "It's the first day!" + Style.RESET_ALL)
	elif call == '>':
		print(Back.RED + Fore.Black + "It's the last day!" + Style.RESET_ALL)
	elif call == 'break':
		break


