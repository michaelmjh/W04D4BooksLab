from db.run_sql import run_sql

from models.book import Book
from models.author import Author
import repositories.author_repository as author_repository

# create book
def save(book):
    sql = "INSERT INTO books (title, author_id) VALUES (?, ?) RETURNING *"
    values = [book.title, book.author.id]
    results = run_sql(sql,values)
    id = results[0]['book_id']
    book.book_id = id
    return book

# delete one author
def delete(id):
    sql = "DELETE FROM books WHERE book_id = ?"
    values = [id]
    run_sql(sql, values)

# delete all books
def delete_all():
    sql= "DELETE FROM books"
    run_sql(sql)

# view all books
def select_all():
    books = []

    sql = "SELECT * FROM books"
    results = run_sql(sql)

    for row in results:
        author = author_repository.select(row['author_id'])
        book = Book(row['title'], author, row['book_id'])
        books.append(book)
    return books    

# view one
def select(id):
    book = None
    sql = "SELECT * FROM books WHERE book_id = ?"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        author = author_repository.select(result['author_id'])
        book = Book(result['title'], author, result['book_id'])
    return book

# edit book
def update(book):
    sql = "UPDATE books SET (title, author_id) = (?, ?) WHERE book_id = ?"
    values = [book.title, book.author.id, book.id]
    run_sql(sql, values)