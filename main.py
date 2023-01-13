from info import key
from func import *


if __name__ == '__main__':
    name = input('Input city in english: ')
    get_url(name, key)
    base_data()
    get_city_temp()
    get_city_wind()

