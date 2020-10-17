import requests
import argparse
import pprint


def init_args():
    """Defines command line arguments.

    Returns:
        ArgumentParser: argument parser that contains the specified arguments.
    """
    helper = 'Retrieves the current weather data from the api.openweathremap.org server.'
    parser = argparse.ArgumentParser(description=helper)

    parser.add_argument(
        'city', type=str, help='The name of the city to get weather for.')
    parser.add_argument('-v', '--verbose', action='store_true',
                        help='displays more weather data')

    return parser


def get_weather_data(city, *args, **kwargs):
    API_KEY = "7f470030130dcc86a0ec2e4869420ac1"
    URL = f"http://api.openweathermap.org/data/2.5/weather?"\
        f"q={city}&"\
        f"appid={API_KEY}"
    print(URL)
    data = requests.get(URL).json()
    return data


def print_weather_data(data):

    pass


if __name__ == "__main__":
    data = get_weather_data(city='London')
    if data['cod'] != 200:
        print(f"Error accured: {data['message']} ❌")
        exit(0)
    elif data['cod'] == 200:
        pprint.pprint(data)
