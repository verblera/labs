"""
Update all films in the film table to a rental_duration value of 10,
if the length of the movie is more than 150.

"""

import sqlalchemy
import sqlite3
from pprint import pprint
engine = sqlalchemy.create_engine('sqlite:///sakila.db')
connection = engine.connect()
metadata = sqlalchemy.MetaData()

film = sqlalchemy.Table('film', metadata, autoload=True, autoload_with=engine)
query = sqlalchemy.update(film).values(rental_duration=10).where(film.columns.length > 150)
result = connection.execute(query)
query = sqlalchemy.select([film]).where(film.columns.length > 150)
result_proxy = connection.execute(query)
result_set = result_proxy.fetchall()
pprint(result_set)