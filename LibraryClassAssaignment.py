"""
Create a Library class with following interface:

- constructor, which will create an instance of Library class. If no arguments are give, an empty collection of books
should be created. If list of books are given as a parameter to the method, each book from the list should be added
to the collection of books.

- an attribute number_of_books should return current number of books in the collection

- add_book(book) method should add a book to the collection if the book does not exist in the collection of books

- borrow_book(book) method should remove a book from the collection if the book is in the collection of books

- show_books() method should print to the console all books, which are in the collection of books
"""


class Library(object):

    def __init__(self, books=None):
        self.book_list = []
        if books:
            for book in books:
                self.add_book(book)

    def add_book(self, book):
        if book:
            if book in self.book_list:
                print('This book is already in the list')
            else:
                self.book_list.append(book)
                print(f"The book {book} is added to the library")
        else:
            print("Enter a book name")

    def borrow_book(self, book):
        if book:
            if book not in self.book_list:
                print("This is not in the list")
            else:
                self.book_list.remove(book)
        else:
            print("Enter a book name")

    def show_books(self):
        for book in self.book_list:
            print(book + '\n')

    def number_of_book(self):
        return len(self.book_list)


my_library = Library()


my_library.add_book('Python')
my_library.add_book('C#')
my_library.add_book('C++')


print(my_library.show_books())
print(my_library.number_of_book())


my_library.borrow_book('C++')


print(my_library.show_books())
print(my_library.number_of_book())
