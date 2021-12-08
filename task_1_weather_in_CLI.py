import requests


def main():

    payload = {
        "Tmnq": "",
        "lang": "ru",
    }

    cities = (
        "Лондон",
        "svo",
        "Череповец",
    )


    for city in cities:
        response = requests.get(f"https://wttr.in/{city}" , params=payload)
        if response.ok:
            print(response.text)
        else:
            print(response.raise_for_status())


if __name__ == "__main__":
    main()
