from getting_data import news_agencies
import sqlalchemy
import sqlite3
from pprint import pprint


engine = sqlalchemy.create_engine('sqlite:///news.db')
connection = engine.connect()
metadata = sqlalchemy.MetaData()

#id,name,description, url, category, language, country
users = sqlalchemy.Table('sources', metadata,

                           sqlalchemy.Column('id',  sqlalchemy.String(255), primary_key=True),
                           sqlalchemy.Column('name', sqlalchemy.String(255)),
                           sqlalchemy.Column('description', sqlalchemy.String(255)),
                           sqlalchemy.Column('url', sqlalchemy.String(255)),
                           sqlalchemy.Column('category', sqlalchemy.String(255)),
                           sqlalchemy.Column('language', sqlalchemy.String(255)),
                           sqlalchemy.Column('country', sqlalchemy.String(255)),
                           )


metadata.create_all(engine)

sources = sqlalchemy.Table('sources', metadata, autoload=True, autoload_with=engine)

query_insert = sqlalchemy.insert(sources)
result_proxy_users = connection.execute(query_insert, news_agencies)

query_select = sqlalchemy.select([sources])
result_proxy = connection.execute(query_select)
result_set = result_proxy.fetchmany(5)
print('Here are 5 sources: ')
pprint(result_set)