import requests
import pprint
import random as ran
import json
import datetime
import pyttsx3
from colorama import init, Fore, Back, Style
init()
golos = pyttsx3.init()
golos.setProperty('rate', 120)

city = 'Kiev' #city
API_KEY = 'd8f1728f479da18a52e428f97e8aac71' #open weather API-Key
hours = {'00': 0, '03': 1, '06': 2, '09': 3, '12': 4, '15': 5, '18': 6, '21': 7} #all avaible times using 5-days sub

response = requests.get(f'https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric') #getting info
response = response.json() #making JSON
hour_now = hours[response['list'][0]['dt_txt'][11:13]] #what's hour now
day_now = response['list'][0]['dt_txt'][5:10] #now we dont need it
dates = []#dates of all days
all_info = [{'humidity': [], 'min_temp': [], 'max_temp': [], 'av_temp': []}, {'humidity': [], 'min_temp': [], 'max_temp': [], 'av_temp': []}, {'humidity': [], 'min_temp': [], 'max_temp': [], 'av_temp': []}, {'humidity': [], 'min_temp': [], 'max_temp': [], 'av_temp': []}, {'humidity': [], 'min_temp': [], 'max_temp': [], 'av_temp': []}]

#func that searches a random advice for our weather
def search_advice(weather_id, descriptions_advices = {'200,201,202': ['Take an umbrella, or beter stay home!'], '210,211,212,221': ["Dont leave your home, it's a little windy!"], '230,231,232': ['Just wait fot the and of this desaster!'], '300,301,302': ['No comments.'], '310,311,312': ["Take an umbrella, or u will have a little shower outside!)"], '313,314': ['Eeeeeeemmm...\n Big... no.\nVery big shower!'], '321': ['Idk.'], '500,501,502,503,504': ['Just a rain, maybee big...\nBut just a rain.'], '511': ['If u go out now, u will become a wet icicle;)'], '520,521,522,531': ['Rain like a shower...\nIdk ;)'], '600,601,602': ["Is it winter?\nI don't know.\nBut today u can make a snowman!\nNICE)"], '611': ['Baby by snow and rain.\nBe carefull there can be ice under snow!'], '612,613': ['Rain thet is very close to snow.'], '615,616': ['NC'], '620,621,622': ['620, 621, 622 Idk'], '701,711,721,731,741,751,761': ['Pls be very carefully, visibility is close to zero.'], '762': ['Zero visibility, and toxic ash in the air!'], '771': ['771 idk'], '781': ['A very high air cone that breaks everything in its path!'], '800': ["Nice day, do'nt forget your sunglasses.\nAnd enjoy having a walk.(800)"], '801': ["Nice day, do'nt forget your sunglasses.\nAnd enjoy having a walk.(801)"], '802,803': ["It's cloudy a little, aand u don't need a sunglasses!"], '804': ['Too much clouds. Maybee the weather will become worser.']}):
    for i in descriptions_advices.keys():
        if str(weather_id) in i:
            key = i
    return f'\n{ran.choice(descriptions_advices[key])}'


def make_data(all_info):
    pass


for i in range(len(response['list'][0:7-hour_now+1])): #making first day's weather dict
    weather_now = response['list'][i]['main']
    min_t_now = weather_now['temp_min']
    max_t_now = weather_now['temp_max']
    humidity_now = weather_now['humidity']
    description_now = response['list'][i]['weather'][0]['description']
    id_now = response['list'][i]['weather'][0]['id']

    if response['list'][0]['dt_txt'][:10] not in dates:
            dates.append(response['list'][0]['dt_txt'][:10])
    all_info[0]['humidity'].append(int(humidity_now))
    all_info[0]['min_temp'].append(int(min_t_now))
    all_info[0]['max_temp'].append(int(max_t_now))
    all_info[0]['description'] = description_now
    all_info[0]['sunrise'] = datetime.datetime.utcfromtimestamp(response['city']['sunrise'])
    all_info[0]['sunset'] = datetime.datetime.utcfromtimestamp(response['city']['sunset'])
    all_info[0]['sunrise'] = f"{all_info[0]['sunrise']}"[10:]
    all_info[0]['sunset'] = f"{all_info[0]['sunset']}"[10:]


response['list'] = response['list'][8-hour_now::] #deleting parsed info
g = 0
for i in range(1, 5): #making other day's weather dict
    for j in range(0, 8):
        k = (i-1)*7+j
        weather_now = response['list'][k]['main']
        min_t_now = weather_now['temp_min']
        max_t_now = weather_now['temp_max']
        humidity_now = weather_now['humidity']
        description_now = response['list'][(i-1)*7+4]['weather'][0]['description']
        if response['list'][k]['dt_txt'][:10] not in dates:
            dates.append(response['list'][k]['dt_txt'][:10])
        all_info[i]['humidity'].append(int(humidity_now))
        all_info[i]['min_temp'].append(float(min_t_now))
        all_info[i]['max_temp'].append(float(max_t_now))
        all_info[i]['description'] = description_now


day = 0
hour = hour_now

for i in range(0, 5):
    all_info[i]['av_temp'] = str((sum(all_info[i]['min_temp']) + sum(all_info[i]['max_temp'])) / float(len(all_info[i]['min_temp']) + len(all_info[i]['min_temp'])))[:5]
    all_info[i]['min_temp'] = str(min(all_info[i]["min_temp"]))
    all_info[i]['max_temp'] = str(max(all_info[i]["max_temp"]))
    all_info[i]['humidity'] = str(sum(all_info[i]['humidity']) / len(all_info[i]['humidity']))[:5]


def pogoda(all_info, dates):
    j = 0
    for i in range(len(all_info)):
        spaces_date = int((30-len(dates[j])-2)/2)+1
        print(' ' + '_'*30 + '\n' + '|' + ' '*spaces_date + dates[j] + ' '*spaces_date + '|' + '\n' + '|' + '_'*30 + '|')
        print('|' + ' '*30 + '|')
        for key, value in all_info[i].items():
            spaces = 30-len(value)-len(key)-2
            print(f"|{key}: {value}{' '*spaces}|")
        print('|' + '_'*30 + '|' + '\n')
        j += 1
    golos.say(f"It's {all_info[0]['av_temp']} grads today (avarage temperature). {all_info[0]['humidity']} percents humidity. The today's weather is {all_info[0]['description']}.")
    golos.runAndWait()
    golos.say(f"It's {all_info[1]['av_temp']} grads tomorow (avarage temperature). {all_info[1]['humidity']} percents humidity. The tomorow's weather is {all_info[1]['description']}.")
    golos.runAndWait()

def main_menu():
    controls = {' weather': '0','exchange': '1', 'exit': 'e'}
    print(' ' + '_'*30)
    print('|' + '   inputput num to view info' + '  ' + '|')
    print('|' + '_'*30 + '|')
    for key, value in controls.items():
        spaces = int((30 - len(key+value))/2)
        print(f'|{" "*spaces}{key}: {value}{" "*(spaces-1)}|')
    print('|' + '_'*30 + '|')
    return input('')


def exchange(date):
    date = '.'.join(date.split('-')[::-1])
    response = requests.get(f'https://api.privatbank.ua/p24api/exchange_rates?json&date={date}').json()['exchangeRate'][1:]
    for i in response:
        if i['currency'] == 'RUB':
            rub = [i['saleRate'], i['purchaseRate']]
        elif i['currency'] == 'EUR':
            eur = [i['saleRate'], i['purchaseRate']]
        elif i['currency'] == 'USD':
            usd = [i['saleRate'], i['purchaseRate']]

    print(f" {'_'*30}")
    print(f"|{' '*13}UAH{' '*14}|")
    print(f"|{'_'*30}|")
    print(f"|{' '*3}RUB{' '*3}|{' '*3}EUR{' '*4}|{' '*3}USD{' '*3}|")
    print(f"|{rub[0]}-{rub[1]}|{eur[0]}-{eur[1]} |{usd[0]}-{usd[1]}|")
    print(f"|b{'_'*7}s|b{'_'*8}s|b{'_'*7}s|\n")
    golos.say(f"RUB to UAH: {rub[0]} to {rub[1]}")
    golos.runAndWait()
    golos.say(f"euro to UAH: {eur[0]} to {eur[1]}")
    golos.runAndWait()
    golos.say(f"american dollar to UAH: {usd[0]} to {usd[1]}")
    golos.runAndWait()


while True:
    search = main_menu()
    if search == '0':
        pogoda(all_info, dates)
    elif search == '1':
        exchange(dates[0])
    elif search == 'e':
        break
    else:
        continue
