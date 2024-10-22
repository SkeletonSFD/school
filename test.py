import requests

places_database =['san francisco',
               'london',
               'svo',
               'череповец'
]

parametrs = {'n_Tnqm&lang':'ru'}

for cities_places in places_database:
    weather_forecast = requests.get(f'https://wttr.in/{cities_places}',params = parametrs)
    weather_forecast.raise_for_status()
    print(weather_forecast.text)

 #'https://wttr.in/san%20francisco?n_Tnqm&lang=ru'
 #https://www.youtube.com/watch?v=2AyV7L7ptHQ
