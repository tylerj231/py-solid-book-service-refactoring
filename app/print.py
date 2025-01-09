from abc import ABC, abstractmethod


class Print(ABC):
    @abstractmethod
    def print(self):
        pass

class PrintConsole(Print):
    def __init__(self, book):
        self.book = book

    def print(self):
        print(f"Printing the book: {self.book.title}...")
        print(self.book.content)

class PrintReverse(Print):
    def __init__(self, book):
        self.book = book

    def print(self):
        print(f"Printing the book in reverse: {self.book.title}...")
        print(self.book.content[::-1])