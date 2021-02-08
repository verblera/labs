"""
Write a program that makes a DELETE request to remove the user your create in a previous example.

Again, make a GET request to confirm that information has been deleted.

"""

import requests

url = 'http://demo.codingnomads.co:8080/tasks_api/users'
url_delete = url + '/285'
response1 = requests.delete(url_delete)
response2 = requests.get(url)
print(response2.json())