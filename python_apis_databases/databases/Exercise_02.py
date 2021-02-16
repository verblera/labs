"""
Consider each of the tasks below as a separate database query. Using SQLAlchemy, which is the necessary code to:

- Select all the actors with the first name of your choice

- Select all the actors and the films they have been in

- Select all the actors that have appeared in a category of a comedy of your choice

- Select all the comedic films and sort them by rental rate

- Using one of the statements above, add a GROUP BY statement of your choice

- Using one of the statements above, add a ORDER BY statement of your choice

"""

import sqlalchemy
import sqlite3
from pprint import pprint
engine = sqlalchemy.create_engine('sqlite:///sakila.db')
connection = engine.connect()
metadata = sqlalchemy.MetaData()

#actors where first_name=
actor = sqlalchemy.Table('actor', metadata, autoload=True, autoload_with=engine)
query = sqlalchemy.select([actor]).where(actor.columns.first_name == 'ED')
result_proxy = connection.execute(query)
result_set = result_proxy.fetchall()
print('actors with name Ed')
pprint(result_set)

#adding order by
query = sqlalchemy.select([actor]).where(actor.columns.first_name == 'ED').order_by(sqlalchemy.asc(actor.columns.last_name))
result_proxy = connection.execute(query)
result_set = result_proxy.fetchall()
print('Ordered Eds')
pprint(result_set)

#actors+their films
film = sqlalchemy.Table('film', metadata, autoload=True, autoload_with=engine)
film_actor = sqlalchemy.Table('film_actor', metadata, autoload=True, autoload_with=engine)
join_statement = actor.join(film_actor, film_actor.columns.actor_id == actor.columns.actor_id).join(film, film.columns.film_id == film_actor.columns.film_id)
query = sqlalchemy.select([film.columns.film_id, film.columns.title,actor.columns.first_name, actor.columns.last_name]).select_from(join_statement)
result_proxy = connection.execute(query)
result_set = result_proxy.fetchmany(30)
print('actors and their films: ')
pprint(result_set)
#adding group by
query = sqlalchemy.select([film.columns.film_id, film.columns.title,actor.columns.first_name,
        actor.columns.last_name]).select_from(join_statement).group_by(actor.columns.last_name)
result_proxy = connection.execute(query)
result_set = result_proxy.fetchmany(30)
print('Grouped actors')
pprint(result_set)

#actors in comedy, rating G
film_category = sqlalchemy.Table('film_category', metadata, autoload=True, autoload_with=engine)
category = sqlalchemy.Table('category', metadata, autoload=True, autoload_with=engine)
join_statement = film.join(film_category,
                film_category.columns.film_id == film.columns.film_id).join(category,
                film_category.columns.category_id == category.columns.category_id).join(film_actor,
                film.columns.film_id == film_actor.columns.film_id).join(actor,
                film_actor.columns.actor_id == actor.columns.actor_id)

query = sqlalchemy.select([actor.columns.last_name,
    film.columns.rating,
    category.columns.name]).select_from(join_statement).where(
    sqlalchemy.and_(category.columns.name=='Comedy', film.columns.rating=='G'))
result_proxy = connection.execute(query)
result_set = result_proxy.fetchall()
print('Actors in G comedies')
pprint(result_set)



#comedy film sort by rental rate
join_statement = film.join(film_category,
                film_category.columns.film_id == film.columns.film_id).join(category,
                film_category.columns.category_id == category.columns.category_id)
query = sqlalchemy.select([film.columns.title,
    film.columns.rental_rate,
    category.columns.name]).select_from(join_statement).where(category.columns.name=='Comedy').order_by(sqlalchemy.desc(film.columns.rental_rate))
result_proxy = connection.execute(query)
result_set = result_proxy.fetchmany(10)
print('10 top rated comedies')
pprint(result_set)




