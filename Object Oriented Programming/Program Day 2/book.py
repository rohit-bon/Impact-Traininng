class Book():
    library_name = "Parul Library"
    
    def __init__(self,book_name,author_name,number_of_pages,book_cost):
        self.book_name = book_name
        self.author_name = author_name
        self.number_of_pages = number_of_pages
        self.book_cost = book_cost
        
    def display(self):
        print(Book.library_name)
        print("Book Name:",self.book_name)
        print("Author Name:",self.author_name)
        print("Number of pages:",self.number_of_pages)
        print("Cost of book:",self.book_cost)
        
n = int(input("Enter Number of Books:"))
i=1
while(i <= n):
    book_name = input("Enter Book Name:")
    author_name = input("Enter Author Name:")
    number_of_pages = input("Enter NUmber of pages:")
    book_cost = input("Enter cost:")
    
    book_obj = Book(book_name,author_name,number_of_pages,book_cost)
    book_obj.display()
    print("*************************************")
    i+=1
    
# o/p:
# Enter Number of Books:2
# Enter Book Name:PIC
# Enter Author Name:kanetkar
# Enter NUmber of pages:300
# Enter cost:100
# Parul Library
# Book Name: PIC
# Author Name: kanetkar
# Number of pages: 300
# Cost of book: 100
# *************************************
# Enter Book Name:cpp
# Enter Author Name:kanetkar
# Enter NUmber of pages:400
# Enter cost:150
# Parul Library
# Book Name: cpp
# Author Name: kanetkar
# Number of pages: 400
# Cost of book: 150