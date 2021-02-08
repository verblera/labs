"""
Building on the previous example, create a list of all of the emails of the users and print
the list to the console.

"""
import requests

url = 'http://demo.codingnomads.co:8080/tasks_api/users'
body = requests.get(url).json()
for user in body['data']:
    print(user['email'])

