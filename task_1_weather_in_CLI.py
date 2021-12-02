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
