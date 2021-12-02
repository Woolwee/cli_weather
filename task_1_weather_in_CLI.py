import requests
import urllib


cities = [
    "Лондон",
    "svo",
    "Череповец",
]


if __name__ == "__main__":
    for city in cities:
        city = urllib.parse.quote(city)
        print(requests.get(f"https://wttr.in/{city}?nTqm&lang=ru").text)

'''
For some reason "Haze" is not translated, 
checked github of wttr.in and didn't find haze translation for Russian and Norwegian languages (jsut e.g.)
https://github.com/chubin/wttr.in/blob/master/share/translations/ru.txt
#        print(requests.get(f"https://wttr.in/{city}?nTqm&lang=ru").text.replace("Haze", "Туман"))
works ofc, but it's crutch for sure
'''
