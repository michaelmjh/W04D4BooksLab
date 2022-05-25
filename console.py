import pdb
from models.book import Book
from models.author import Author


import repositories.author_repository as author_repository
import repositories.book_repository as book_repository


# author_repository.delete_all()
# book_repository.delete_all()

author_1 = Author("Nick", "Hornby")
author_repository.save(author_1)

# author_2 = Author("Bret Easton", "Ellis")
# author_repository.save(author_2)

# author_3 = Author("Belinda", "Bauer")
# author_repository.save(author_3)

book_1 = Book("High Fidelity", author_1)
book_repository.save(book_1)

# book_2 = Book("American Psycho", author_2)
# book_repository.save(book_2)

# book_3 = Book("Exit", author_3)
# book_repository.save(book_3)


# authors = author_repository.select_all()
# for author in authors: 
#     print (author.__dict__)

# # author = author_repository.select(1)
# # print (author.__dict__)

# author_1 = Author("John", "Jenkins", 3)
# author_repository.update(author_1)
# author_repository.delete(1)
# book_repository.delete(6)

authors=author_repository.select_all()
for author in authors: 
    print (author.__dict__)


# book_1 = Book("SQL Programming", author_1, 7)
# book_repository.update(book_1)

books = book_repository.select_all()
for book in books:
    print(book.__dict__)

# book = book_repository.select(7)
# print(book.__dict__)










pdb.set_trace()