# MINI PROJECT : Smart Weather System
print("\nMINI PROJECT : Smart Weather System ")

import requests


def get_weather_condition(code):

    if code == 0:
        return "Clear Sky"

    elif code in [1, 2, 3]:
        return "Cloudy"

    elif code in [45, 48]:
        return "Fog"

    elif code in [51, 53, 55]:
        return "Drizzle"

    elif code in [61, 63, 65]:
        return "Rain"

    elif code in [71, 73, 75]:
        return "Snow"

    elif code in [95, 96, 99]:
        return "Thunderstorm"

    else:
        return "Unknown"



def search_weather():

    city = input("\nEnter City: ").strip()

    if not city:
        print("Please enter a city name!")
        return None


    try:
        geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"

        geo_response = requests.get(geo_url , timeout= 10)

        geo_response.raise_for_status()
        print(f"\nGeocoding API Status Code : {geo_response.status_code}")

        geo_data = geo_response.json()


        if "results" not in geo_data   or not geo_data['results']:
            print("City Not Found!!")
            return None


        lat = geo_data["results"][0]["latitude"]
        lon = geo_data["results"][0]["longitude"]
        print(f"\nLatitude     : {lat}"
              f"\nLongitude  : {lon}")

        weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,relative_humidity_2m,weather_code,wind_speed_10m"

        weather_response = requests.get(weather_url , timeout = 10)

        weather_response.raise_for_status()
        print(f"\nWeather API Status Code : {weather_response.status_code}")

        weather_data = weather_response.json()


        clean_data = {
            "city" : city ,
            "temp" : weather_data['current']['temperature_2m'],
            "humidity" : weather_data['current']['relative_humidity_2m'],
            "condition" : weather_data['current']['weather_code'],
            "wind" : weather_data['current']['wind_speed_10m']

        }

        return clean_data

    except requests.exceptions.Timeout:
        print("\nConnection Timeout Error!!")
        return None

    except requests.exceptions.ConnectionError:
        print("\nUnable to Connect To the API!!")
        return None

    except requests.exceptions.HTTPError as http_err:
        print(f"\nError Code : {http_err}")
        return None

    except requests.exceptions.RequestException as err:
        print(f"\nError : {err}")

        return None


def view_result(clean_data):
    print("===================================")
    print("       Smart Weather System        ")
    print("===================================")

    print("\nWeather Information")
    print(f"\nCity          : {clean_data['city']}")
    print(f"Temperature   : {clean_data['temp']}")
    print(f"Humidity      : {clean_data['humidity']}")
    print(f"Condition     : {clean_data['condition']}")
    print(f"Wind Speed    : {clean_data['wind']}")


last_result = None
while True:
    print("\n======= Smart Weather System =========")
    print("\nSelect an Option")
    print("\n1. Search Weather")
    print("2. View Last Result")
    print("3. Exit")

    try:
        option = int(input("Enter Your Option:"))

    except ValueError:
        print("Invalid Option!")
        continue

    if option == 1:
        last_result = search_weather()

        if last_result is not None:
            print("\nWeather data saved successfully!")

    elif option == 2:
        if last_result is None:
            print("No data yet, please search first")
        else:
            view_result(last_result)

    elif option == 3:
        print("Exiting..... ")
        break

    else:
        print("Invalid Option!")