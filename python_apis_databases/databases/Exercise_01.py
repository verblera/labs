"""

All of the following exercises should be done using sqlalchemy.

Using the provided database schema, write the necessary code to print information about the film and category table.

"""

import sqlalchemy
import sqlite3
from pprint import pprint
engine = sqlalchemy.create_engine('sqlite:///sakila.db')
connection = engine.connect()
metadata = sqlalchemy.MetaData()

film = sqlalchemy.Table('film', metadata, autoload=True, autoload_with=engine)
film_category = sqlalchemy.Table('film_category', metadata, autoload=True, autoload_with=engine)
category = sqlalchemy.Table('category', metadata, autoload=True, autoload_with=engine)
#print(film.columns.keys())
join_statement = film.join(film_category, film_category.columns.film_id == film.columns.film_id).join(category, category.columns.category_id == film_category.columns.category_id)
query = sqlalchemy.select([film.columns.title, category.columns.name]).select_from(join_statement)
result_proxy = connection.execute(query)
result_set = result_proxy.fetchmany(15)
pprint(result_set)

