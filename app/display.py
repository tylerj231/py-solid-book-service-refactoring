from abc import ABC, abstractmethod

class Display(ABC):
    @abstractmethod
    def display(self):
        pass

class ConsoleDisplay(Display):
    def __init__(self, book):
        self.book = book

    def display(self):
        print(self.book.content)

class ReverseDisplay(Display):
    def __init__(self, book):
        self.book = book

    def display(self):
        print(self.book.content[::-1])
