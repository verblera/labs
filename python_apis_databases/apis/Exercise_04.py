"""
Write a program that makes a PUT request to update your user information to a new first_name, last_name and email.

Again make a GET request to confirm that your information has been updated.

"""

import requests

url = 'http://demo.codingnomads.co:8080/tasks_api/users'
body = {"id": 285,
        "first_name": "Adam",
        "last_name": "Smith",
        "email": "not-typical@email.com"}
response1 = requests.put(url, json=body)
response2 = requests.get(url)
print(response2.json())