# pylint: disable=missing-docstring, C0103
import sqlite3

conn = sqlite3.connect('data/movies.sqlite')

# => list (rows) of tuples (columns)

def directors_count(db):
    # return the number of directors contained in the database
    db.execute("SELECT COUNT(id) FROM directors")
    results = db.fetchall()
    # results in a list (rows) of tuples (columns)
    print(results)  # Inspect what you get back! Don't guess!
    # Then you'll need to return something.
    return int(results[0][0])


def directors_list(db):
    # return the list of all the directors sorted in alphabetical order
    db.execute("SELECT directors.name FROM directors  ORDER BY name ASC")
    results = db.fetchall()
    # results in a list (rows) of tuples (columns)
    print(results)  # Inspect what you get back! Don't guess!
    # Then you'll need to return something.
    return [row[0] for row in results]


def river_movies(db):
    # return the list of all movies which contain the exact word "river"
    # in their title, sorted in alphabetical order
    db.execute("""SELECT title FROM movies WHERE UPPER(title) LIKE '% river %'
               OR title LIKE 'river %' OR title LIKE '% river' OR title
               LIKE 'river' ORDER BY title ASC""")
    results = db.fetchall()

    return [result[0] for result in results]


def directors_named_like_count(db, name):
    # return the number of directors which contain a given word in their name
    query = "SELECT COUNT(id) FROM directors WHERE name LIKE ?"
    db.execute(query, (f"%{name}%",))
    result = db.fetchone()
    return int(result[0])


def movies_longer_than(db, min_length):
    # return this list of all movies which are longer than a given duration,
    # sorted in the alphabetical order

    db.execute("SELECT title FROM movies WHERE minutes > ? ORDER BY title ASC", (min_length,))
    results = db.fetchall()
    # Then you'll need to return something.
    return [row[0] for row in results]
