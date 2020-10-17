"""
    This is a command line tool for using the openweathermap.org API.
    - Retrieving current weather of a specified city or cities,
    - Easy way and no complicated libraries.
    - Provides saving the data in a JSON format.
"""

import os
import requests
import argparse
import pprint


def init_args():
    """Defines command line arguments.

    Returns:
        ArgumentParser: argument parser that contains the specified arguments.
    """
    helper = 'Retrieves the current weather data from the api.openweathremap.org server of the given city.'
    parser = argparse.ArgumentParser(description=helper)

    parser.add_argument(
        'city', type=str, help='the name of the city to get weather for.')
    parser.add_argument('-v', '--verbose', action='store_true',
                        help='displays more weather data')
    parser.add_argument('-u', '--units', action='store',
                        help='for temperature in Fahrenheit use "imperial", for temperature in Celsius use "metric", temperature in Kelvin is used by default, no need to use units parameter in API call.')

    return parser


def get_weather_data(city, units, *args, **kwargs):
    """Retrieves the weather data of the given city name from 'api.openweathermap.org'.

    Args:
        city (string): CITY ID, or a list of cities names.
        units (string): for temperature in Fahrenheit use "imperial", for temperature in Celsius use "metric", temperature in Kelvin is used by default, no need to use units parameter in API call.


    Returns:
        dict: A dictionary contains all data about the weather of the given city(ies)
    """
    API_KEY = os.environ['WEATHER_API_KEY']
    URL = f"http://api.openweathermap.org/data/2.5/weather?"
    URL += f"q={city}&"
    # use units argument if specified
    if units != "":
        URL += f"units={units}&"
    URL += f"appid={API_KEY}"
    data = requests.get(URL).json()

    return data


def print_weather_data(data):
    info = f"""\
    ------------------------------
    City    : {data['name']}
    Country : {data['sys']['country']}
    ------------------------------
    Temperature : {data['main']['temp']} ({data['main']['temp_min']}/{data['main']['temp_max']})
    Pressure    : {data['main']['pressure']} 
    Humidity    : {data['main']['humidity']} 
    """
    return info


if __name__ == "__main__":
    # argument parser
    parser = init_args()
    # get cli arguments
    args = parser.parse_args()

    data = get_weather_data(city=args.city, units=args.units)
    if data['cod'] != 200:
        print(f"Error accured: {data['message']} ❌")
        exit(0)
    elif data['cod'] == 200:
        print(print_weather_data(data))
