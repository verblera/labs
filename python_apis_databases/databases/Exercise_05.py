"""
Using the API from the API section, write a program that makes a request to
get all of the users and all of their tasks.

Create tables in a new local database to model this data.

Think about what tables are required to model this data. Do you need two tables? Three?

Persist the data returned from the API to your database.

NOTE: If you run this several times you will be saving the same information in the table.
To prevent this, you should add a check to see if the record already exists before inserting it.

"""
import requests
import sqlalchemy
import sqlite3
from pprint import pprint



#fetching data about users in json:
url_users = 'http://demo.codingnomads.co:8080/tasks_api/users'
response = requests.get(url_users).json()

#getting a list of users with their data, but won't use it later
list_users = []
for user in response['data']:
    list_users.append(user) #getting dictionary
#fetching data about tasks in json:
url_tasks = 'http://demo.codingnomads.co:8080/tasks_api/tasks'
body = requests.get(url_tasks).json()

#getting a list of tasks with their data, but won't use it later
list_tasks = []
for task in body['data']:
    list_tasks.append(task) #getting dictionary


#connecting to a database/creating it:
engine = sqlalchemy.create_engine('sqlite:///tasks_users.db')
connection = engine.connect()
metadata = sqlalchemy.MetaData()


#deleting tables from previous attempts if exist:
try:
    query = sqlalchemy.delete(tasks)
    result_proxy = connection.execute(query)
except NameError:
    pass
try:
    query = sqlalchemy.delete(users)
    result_proxy = connection.execute(query)
except NameError:
    pass

#creating two tables for each apis
users = sqlalchemy.Table('users', metadata,

                           sqlalchemy.Column('id', sqlalchemy.Integer()),
                           sqlalchemy.Column('first_name', sqlalchemy.String(255)),
                           sqlalchemy.Column('last_name', sqlalchemy.String(255)),
                           sqlalchemy.Column('email', sqlalchemy.String(255)),
                           sqlalchemy.Column('createdAt', sqlalchemy.String(255)),
                           sqlalchemy.Column('updatedAt', sqlalchemy.String(255))
                           )

tasks = sqlalchemy.Table('tasks', metadata,

                           sqlalchemy.Column('id', sqlalchemy.Integer()),
                           sqlalchemy.Column('userId', sqlalchemy.Integer()),
                           sqlalchemy.Column('name', sqlalchemy.String(255)),
                           sqlalchemy.Column('description', sqlalchemy.String(255)),
                           sqlalchemy.Column('createdAt', sqlalchemy.String(255)),
                           sqlalchemy.Column('updatedAt', sqlalchemy.String(255)),
                           sqlalchemy.Column('completed', sqlalchemy.Boolean())
                           )

metadata.create_all(engine)

#opening tables
tasks = sqlalchemy.Table('tasks', metadata, autoload=True, autoload_with=engine)
users = sqlalchemy.Table('users', metadata, autoload=True, autoload_with=engine)


#adding users to a table
records_users = response['data']
query_users = sqlalchemy.insert(users)
result_proxy_users = connection.execute(query_users, records_users)

#deleting deficient rowas:
query_users = sqlalchemy.delete(users).where(users.columns.first_name=='[YOUR FIRST NAME FIELD]')
result = connection.execute(query_users)

#fetching 5 first rows:
query_users = sqlalchemy.select([users])
result_proxy_users = connection.execute(query_users)
result_set_users = result_proxy_users.fetchmany(5)
print('Here are 5 users: ')
pprint(result_set_users)

#adding tasks:
records_tasks = body['data']
query_tasks = sqlalchemy.insert(tasks)
result_proxy_tasks = connection.execute(query_tasks, records_tasks)

#fetching results:
query_tasks = sqlalchemy.select([tasks])
result_proxy_tasks = connection.execute(query_tasks)
result_set_tasks = result_proxy_tasks.fetchmany(5)
print('Here are 5 tasks: ')
pprint(result_set_tasks)



