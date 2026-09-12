# Program 1: Basic API Request
print("\nProgram 1: Basic API Request")


import requests

try:
    response = requests.get("https://jsonplaceholder.typicode.com/posts/9999" , timeout = 10)
    print(f"\nStatus Code : {response.status_code}")
    print(f"\nText : {response.text}")

except requests.exceptions.ConnectionError:
    print("Unable to  connect  to  the API")

except requests.exceptions.Timeout:
    print("The API request  timed out!!")