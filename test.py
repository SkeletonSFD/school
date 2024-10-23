import requests


places=['san francisco',
               'london',
               'svo',
               'череповец'
]

parameters = {'nTnqm':'',
             'lang':'ru'
}

for place in places:
    weather_forecast = requests.get(f'https://wttr.in/{place}',params = parameters)
    weather_forecast.raise_for_status()
    print(weather_forecast.text)
