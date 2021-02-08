"""
Write the necessary code to make a POST request to:

    http://demo.codingnomads.co:8080/tasks_api/users

and create a user with your information.

Make a GET request to confirm that your user information has been saved.

"""


import requests

url = 'http://demo.codingnomads.co:8080/tasks_api/users'
body = {"first_name": "Adam",
        "last_name": "Smith",
        "email": "typical@email.com"}
response1 = requests.post(url, json=body)
response2 = requests.get(url)
print(response2.json())