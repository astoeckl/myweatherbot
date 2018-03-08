# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 13:15:43 2018

@author: p20133
"""

import requests

city = "London"
r = requests.get("http://samples.openweathermap.org/data/2.5/forecast?q="+city+"&appid=ecd11b887d65ca7a4464cf11f3a90528")
json_object = r.json()
weather = json_object["list"]
condition = weather[1]["weather"][0]["description"]
print(condition)