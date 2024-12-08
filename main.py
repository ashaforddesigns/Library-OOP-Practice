""" Design classes for Book, Member, and Library.
Add attributes and methods based on what you think these entities would need. For example:
Books might have a title, author, and availability status.
Members might have a name and a borrowing limit.
Library might need to manage a collection of books and track transactions. """

class Book:
    def __init__(self, title, author=str, available=bool):
        self.title = title
        self.author = author
        self.available = available
    def search(self):


class Member:
    def __init__(self, name, checkedOut):
        pass

class Library:
    def __init__(self):
        pass
