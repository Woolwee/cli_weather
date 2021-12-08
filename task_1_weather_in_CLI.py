import requests


def main():

    cities = (
        "Лондон",
        "svo",
        "Череповец",
    )

    payload = {
        "Tmnq": "", 
        "lang": "ru",
    }


    for city in cities:
        response = requests.get(f"https://wttr.in/{city}" , params=payload)
        if response.ok:
            print(response.text)
        else:
            print(response.raise_for_status())


if __name__ == "__main__":
    main()
