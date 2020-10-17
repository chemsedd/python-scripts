import requests
import argparse
import pprint


def get_weather_data(city, *args, **kwargs):
    API_KEY = "7f470030130dcc86a0ec2e4869420ac1"
    URL = f"http://api.openweathermap.org/data/2.5/weather?"\
        f"q={city}&"\
        f"appid={API_KEY}"
    print(URL)
    data = requests.get(URL).json()
    return data


if __name__ == "__main__":
    data = get_weather_data(city='London')
    if data['cod'] != 200:
        print(f"Error accured: {data['message']} ❌")
        exit(0)
    elif data['cod'] == 200:
        pprint.pprint(data)
