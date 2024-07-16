from bs4 import BeautifulSoup
import requests
import pycountry
from tempconversion import temp_conversion
import config

def weather(zipcode, country):
    """
    Fetches and displays the weather information for the given zipcode and country.
    Returns: bool, True if the weather data was fetched successfully, False otherwise.
    """

    country = 'US' if country == '' else country
    url = f'https://api.openweathermap.org/data/2.5/weather?zip={zipcode},{country}&appid={config.API_KEY}&mode=xml'
    res = requests.get(url)

    if res.status_code == 200:
        print(f"\nSearching for {zipcode} in {pycountry.countries.get(alpha_2=country).name}...")
        soup = BeautifulSoup(res.text, 'xml')  
        temp_tag = soup.find('temperature')
        if temp_tag is not None:
            temp_value = temp_tag['value']
            temp_unit = temp_tag['unit'][:1]
            print(f"Temperature:\t {temp_conversion(temp_value, temp_unit, 'F')} F / {temp_conversion(temp_value, temp_unit, 'C')} C")
        else:
            print("Temperature information is not found for that zipcode")

        weather_tag = soup.find('weather')
        if weather_tag is not None:
            weather_desc = weather_tag['value']
            print(f"Weather:\t {weather_desc}")
        else:
            print("Weather information is not found for that zipcode")
        return True
    else:
        print("\nError fetching the weather data with the provided zipcode and country combination.")
        return False

def is_valid_country_code(country):
    """Checks if the given two-letter code is a valid ISO 3166-1 alpha-2 country code."""
    try:
        pycountry.countries.get(alpha_2=country)
        return True
    except AttributeError:
        return False
