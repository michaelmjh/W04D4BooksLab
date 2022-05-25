from crypt import methods
from flask import Flask, render_template, request, redirect
from repositories import book_repository, author_repository

from flask import Blueprint
from models.book import Book

books_blueprint = Blueprint("book", __name__)

@books_blueprint.route("/books")
def books():
    books = book_repository.select_all()
    return render_template("books/show_all.html", all_books = books)

@books_blueprint.route("/books/<id>/delete", methods=['POST'])
def delete_book(id):
    book_repository.delete(id)
    return redirect("/books")

@books_blueprint.route("/books/new", methods=['GET'])
def new_book():
    authors = author_repository.select_all()
    return render_template("books/new.html", all_authors=authors)

@books_blueprint.route("/books", methods=['POST'])
def create_book():
    title = request.form['title']
    author_id = request.form['author_id']

    author = author_repository.select(author_id)
    book = Book(title, author)
    book_repository.save(book)

    return redirect('/books')

@books_blueprint.route("/books/<id>", methods=['GET'])
def show_book(id):
    book = book_repository.select(id)
    return render_template('books/show.html', book=book)

@books_blueprint.route("/books/<id>/edit", methods=['GET'])
def edit_book(id):
    book = book_repository.select(id)
    authors = author_repository.select_all()
    return render_template('books/edit.html', book=book, all_authors=authors)

@books_blueprint.route("/books/<id>", methods=['post'])
def update_book(id):
    title = request.form['title']
    author_id = request.form['author_id']
    
    author = author_repository.select(author_id)
    book = Book(title, author, id)

    book_repository.update(book)
    return redirect('/books')