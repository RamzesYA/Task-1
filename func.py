import requests
from datetime import datetime

def output(dict):
    for key, value in dict.items():
        print("{0}: {1}".format(key, value))

def get_url(name, key):

    global updates
    url = f'https://api.openweathermap.org/data/2.5/weather?q={name.lower()}&appid={key}&units=metric'
    updates = requests.get(url).json()

    if updates['cod']!=200:
        print('Wrong city')
        exit()

def base_data():
    date = datetime.fromtimestamp(updates['dt']).strftime('%d-%m-%Y %H:%M:%S')
    print(f'\n{updates["name"]}\n{date}\n')

def get_city_temp():
    answer = {}

    answer['Temperature'] = updates['main']['temp']
    answer['Feels like'] = updates['main']['feels_like']
    output(answer)

def get_city_wind():
    answer = {}

    answer['Wind speed'] = updates['wind']['speed']
    answer['Gusts to'] = updates['wind']['gust']
    output(answer)