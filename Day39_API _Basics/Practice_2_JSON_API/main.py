# Program 2:  JSON API
print("\nProgram 2 : JSON API")


import requests

try:
    response = requests.get("https://jsonplaceholder.typicode.com/users/1" , timeout = 10 )
    print(f"\nStatus Code : {response.status_code}")
    print(f"\nData : {response.text}")

    response.raise_for_status()
    data = response.json()
    print(data)
    print(f"Name : {data['name']}")


except requests.exceptions.ConnectionError:
    print("Unable to connect to the  API")

except requests.exceptions.Timeout:
    print("Timeout Error")

except requests.exceptions.HTTPError as http_err:
    print(f"Error : { http_err}")

except Exception as err:
    print(err)