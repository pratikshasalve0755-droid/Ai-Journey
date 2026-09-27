# Program 3: API Data Analyzer

print("\nProgram 3: API Data Analyzer")


import requests

def fetch_data():
    try:

        response = requests.get("https://jsonplaceholder.typicode.com/users" , timeout = 10)

        response.raise_for_status()
        print(f"\nStatus Code : {response.status_code}")

        data = response.json()
        print(f"\nData : {data}")

        return data

    except requests.exceptions.ConnectionError:
        print("\nUnable to connect the API")

    except requests.exceptions.HTTPError as http_err:
        print(f"\nHTTP error occurred: {http_err}")

    except requests.exceptions.Timeout:
        print("\nAPI took  too long!")

    except Exception as err:
        print(f"Error : {err}")

    return None

def analyze_data(data):

    analyzed_data = []

    for user in data:
        new_user = {
            "id" : user['id'],
            "name" : user['name'],
            "username" : user['username'],
            "email" : user['email'],
            "phone" : user['phone']
        }

        analyzed_data.append(new_user)

    return analyzed_data


def display_data(analyzed_data):
    print("===================================")
    print("        API Data Analyzer   ")
    print("====================================")

    for user in analyzed_data:
        print(f"ID        : {user['id']}")
        print(f"Name      : {user['name']}")
        print(f"Username  : {user['username']}")
        print(f"Email     : {user['email']}")
        print(f"Phone     : {user['phone']}")
        print("--------------------------------")

    print("====================================")


raw_data = fetch_data()
if raw_data:
    analyzed = analyze_data(raw_data)
    display_data(analyzed)







