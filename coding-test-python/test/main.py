# -*- coding: utf-8 -*-
"""
MAIN
"""
import json
import requests
import colorama
from colorama import Fore


def run():
    colorama.init()
    r = requests.get('https://api.chucknorris.io/jokes/random')
    with open('json-joker.json', 'w') as dataFile:
        json.dump(r.json(), dataFile, indent=4)
    txt = open('joker.txt','w')
    rjson=r.json()
    txt.write(rjson['value'])
    print(Fore.BLUE, r.json())
    return 1

