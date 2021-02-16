"""

Please create a new Python application that interfaces with a brand new database.
This application must demonstrate the ability to:

    - create at least 3 tables +
    - insert data to each table +
    - update data in each table +
    - select data from each table +
    - delete data from each table +
    - use at least one join in a select query+

BONUS: Make this application something that a user can interact with from the CLI. Have options
to let the user decide what tables are going to be created, or what data is going to be inserted.
The more dynamic the application, the better!


"""

import sqlalchemy
import sqlite3
from pprint import pprint

engine = sqlalchemy.create_engine('sqlite:///books.db')
connection = engine.connect()
metadata = sqlalchemy.MetaData()
newBook = sqlalchemy.Table('book', metadata,

                           sqlalchemy.Column('book_id', sqlalchemy.Integer()),
                           sqlalchemy.Column('title', sqlalchemy.String(255)),
                           sqlalchemy.Column('author_id', sqlalchemy.Integer()),
                           sqlalchemy.Column('genre_id', sqlalchemy.String(255))
                           )
newAuthor = sqlalchemy.Table('author', metadata,

                             sqlalchemy.Column('author_id', sqlalchemy.Integer()),
                             sqlalchemy.Column('first_name', sqlalchemy.String(255)),
                             sqlalchemy.Column('last_name', sqlalchemy.String(255))
                             )
newGenre = sqlalchemy.Table('genre', metadata,

                            sqlalchemy.Column('genre_id', sqlalchemy.Integer()),
                            sqlalchemy.Column('genre', sqlalchemy.String(255))
                            )
metadata.create_all(engine)

book = sqlalchemy.Table('book', metadata, autoload=True, autoload_with=engine)
genre = sqlalchemy.Table('genre', metadata, autoload=True, autoload_with=engine)
author = sqlalchemy.Table('author', metadata, autoload=True, autoload_with=engine)

records_book = [{'book_id': 1, 'title': 'To Kill a Mockingbird', 'author_id': 1, 'genre_id': 1},
                {'book_id': 2, 'title': 'Pride and Prejudice', 'author_id': 2, 'genre_id': 2},
                {'book_id': 3, 'title': 'The Dutch House', 'author_id': 3, 'genre_id': 1},
                {'book_id': 4, 'title': 'Commonwealth', 'author_id': 3, 'genre_id': 1},
                {'book_id': 5, 'title': 'Crime and Punishment', 'author_id': 4, 'genre_id': 1}]
records_author = [{'author_id': 1, 'first_name': 'Harper', 'last_name': 'Lee'},
                  {'author_id': 2, 'first_name': 'Jane', 'last_name': 'Austen'},
                  {'author_id': 3, 'first_name': 'Ann', 'last_name': 'Patchett'},
                  {'author_id': 4, 'first_name': 'Fedor', 'last_name': 'Dostoevsky'}]
records_genre = [{'genre_id': 1, 'genre': 'Novel'},
                 {'genre_id': 2, 'genre': 'Romance'}]

query_book = sqlalchemy.insert(book)
query_author = sqlalchemy.insert(author)
query_genre = sqlalchemy.insert(genre)

result_proxy_book = connection.execute(query_book, records_book)
result_proxy_author = connection.execute(query_author, records_author)
result_proxy_genre = connection.execute(query_genre, records_genre)
# selecting
query_author = sqlalchemy.select([author])
result_proxy_author = connection.execute(query_author)
result_set_author = result_proxy_author.fetchall()
print('checking if tables were created successfully quering a table author')
pprint(result_set_author)

# update
query_book = sqlalchemy.update(book).values(title='To Kill a Mockingbird II').where(
    book.columns.title == 'To Kill a Mockingbird')
query_author = sqlalchemy.update(author).values(first_name='Fyodor').where(author.columns.first_name == 'Fedor')
query_genre = sqlalchemy.update(genre).values(genre='Thriller').where(genre.columns.genre_id == 1)
result_book = connection.execute(query_book)
result_genre = connection.execute(query_genre)
result_author = connection.execute(query_author)

query_author = sqlalchemy.select([author])
result_proxy_author = connection.execute(query_author)
result_set_author = result_proxy_author.fetchall()
print('Checking updates == Updating Dostoevky\'s name')
pprint(result_set_author)

# join
join_statement = book.join(author,
                           author.columns.author_id == book.columns.author_id).join(genre,
                                                                                    genre.columns.genre_id == book.columns.genre_id)
query = sqlalchemy.select([author.columns.last_name, book.columns.title, genre.columns.genre]).select_from(join_statement)
result_proxy = connection.execute(query)
result_set = result_proxy.fetchall()
print('Author\'s last name, book\'s title and genre')
pprint(result_set)


# deleting all
query_book = sqlalchemy.delete(book)
result_proxy_book = connection.execute(query_book)
# deleting parts
query_genre = sqlalchemy.delete(genre).where(genre.columns.genre_id == 2)
result_proxy_genre = connection.execute(query_genre)

query_author = sqlalchemy.delete(author).where(author.columns.last_name == 'Patchett')
result_proxy_author = connection.execute(query_author)
query_author = sqlalchemy.select([author])
result_proxy_author = connection.execute(query_author)
result_set_author = result_proxy_author.fetchall()
print('Deleting Patchett')
pprint(result_set_author)
