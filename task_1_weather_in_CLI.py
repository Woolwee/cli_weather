import requests


payload = {
    "Tmnq": "", 
    "lang": "ru"
    }

cities = [
    "Лондон",
    "svo",
    "Череповец",
]


def main():
    for city in cities:
        print(requests.get(f"https://wttr.in/{city}" , params=payload).text)


if __name__ == "__main__":
    main()
