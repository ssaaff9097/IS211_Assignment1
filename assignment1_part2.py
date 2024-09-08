class Book:
        def __init__(self, author="", title=""):
            """
            Constructor of a Book's Author and Title
            :param Author: The name of the author
            :param Title: the name of the book
            """
            self.author = author
            self.title = title
    
        def display(self):
            """Display the Book's Author and title"""
            print(f"{self.title}, written by {self.author}")

if __name__ == "__main__":
    Book1 = Book("J. K. Rowling", "Harry Potter and the Goblet of Fire")
    Book2 = Book("Walter Scott", "Ivanhoe: A Romance")

Book1.display()
Book2.display()
