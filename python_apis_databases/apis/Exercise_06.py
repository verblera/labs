"""

Create an application that interfaces with the user via the CLI - prompt the user with a menu such as:

Please select from the following options (enter the number of the action you'd like to take):
1) Create a new account (POST)
2) View all your tasks (GET)
3) View your completed tasks (GET)
4) View only your incomplete tasks (GET)
5) Create a new task (POST)
6) Update an existing task (PATCH/PUT)
7) Delete a task (DELETE)

It is your responsibility to build out the application to handle all menu options above.


"""

import requests
option = 0
while option < 1 or option > 7:
    option = int(input('Please select from the following options (enter the number of the action you\'d like to take): '
                       '\n1) Create a new account (POST)'
                       '\n2) View all your tasks (GET)'
                       '\n3) View your completed tasks (GET)'
                       '\n4) View only your incomplete tasks (GET)'
                       '\n5) Create a new task (POST)'
                       '\n6) Update an existing task (PATCH/PUT)'
                       '\n7) Delete a task (DELETE)\n\n'))

url_user = 'http://demo.codingnomads.co:8080/tasks_api/users'
url = 'http://demo.codingnomads.co:8080/tasks_api/tasks'

if option == 1:
    body = {"first_name": "Adam",
            "last_name": "Smith",
            "email": "typical@email.com"}
    response1 = requests.post(url_user, json=body)
elif option == 2:
    response = requests.get(url)
    print(response.json())
elif option == 3:
    body = requests.get(url).json()
    for task in body['data']:
        if task['completed']:
            print(task)
elif option == 4:
    body = requests.get(url).json()
    for task in body['data']:
        if not task['completed']:
            print(task)
elif option == 5:
    description = input('Please, describe: ')
    name = input('Please, name it: ')
    body = {"completed": 'false',
            "description": description,
            "id": 999,
            "name": name,
            "userId": 1}
    response = requests.post(url, json=body)
elif option == 6:
    description = input('Please, describe: ')
    name = input('Please, name it: ')
    body = {"completed": 'false',
            "description": description,
            "id": 999,
            "name": name,
            "userId": 1}
    response = requests.put(url, json=body)
else:
    url_delete = url + '/999'
    response1 = requests.delete(url_delete)

print('finished')
