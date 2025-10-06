# File: oop/book_class.py

class Book:
    """A class that models a Book using Python magic methods."""

    def __init__(self, title, author, year):
        """Constructor that initializes the book attributes."""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Destructor that notifies when a book instance is deleted."""
        print(f"Deleting {self.title}")

    def __str__(self):
        """User-friendly string representation of the book."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Official representation of the book object."""
        return f"Book('{self.title}', '{self.author}', {self.year})"
