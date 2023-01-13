import requests

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