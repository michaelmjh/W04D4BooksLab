from db.run_sql import run_sql

from models.book import Book
from models.author import Author


# create author
def save(author):
    sql = "INSERT INTO authors (first_name, last_name) VALUES (?, ?) RETURNING *"
    values = [author.first_name, author.last_name]
    results = run_sql(sql,values)
    id = results[0]['author_id']
    author.author_id = id
    return author

# delete one author
def delete(id):
    sql = "DELETE FROM authors WHERE author_id = ?"
    values = [id]
    run_sql(sql, values)

# delete all author
def delete_all():
    sql= "DELETE FROM authors"
    run_sql(sql)

# view all authors
def select_all():
    authors = []

    sql = "SELECT * FROM authors"
    results = run_sql(sql)

    for row in results:
        author = Author(row['first_name'], row['last_name'], row['author_id'])
        authors.append(author)
    return authors    

# view one
def select(id):
    author = None
    sql = "SELECT * FROM authors WHERE author_id = ?"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        author = Author(result['first_name'], result['last_name'], result['author_id'] )
    return author

# edit author
def update(author):
    sql = "UPDATE authors SET (first_name, last_name) = (?, ?) WHERE author_id = ?"
    values = [author.first_name, author.last_name, author.author_id]
    run_sql(sql, values)