# -*- coding: utf-8 -*-

"""
Python OOP example from FreeCodeCamp
"""
#from abc import ABC, abstractmethod

class Book():
    def __init__(self, title, quantity, author, price): # special method used as a constructor to initalize values
        self.__title = title
        self.__quantity = quantity
        self.__author = author
        self.__price = price
        self.__discount = None
    
    # Title getter/setter
    def get_title(self):
        return self.__title
    
    def set_title(self, title):
        self.__title = title
        
    # Quantity getter/setter
    def get_quantity(self):
        return self.__quantity
    
    def set_quantity(self, quantity):
        self.__quantity = quantity

    # Author getter/setter
    def get_author(self):
        return self.__author
    
    def set_author(self, author):
        self.__author = author
                
    # Price getter/setter
    def get_price(self):
        if self.__discount:
            return self.__price * (1 - self.__discount)
        return self.__price    
    
    def set_price(self, price):
        self.__price = price
    
    # Discount getter/setter
    def get_discount(self):
        return self.__discount
    
    def set_discount(self, discount):
        self.__discount = discount
        
    # Display book information - modified to be abstract so that any subclasses that inherit from Book will be
    # required to implement some version of __repr__
    #@abstractmethod
    def __repr__(self):
        return f"Title: {self.get_title()}, Quantity: {self.get_quantity()}, Author: {self.get_author()}, Price: {self.get_price()}, Discount: {self.get_discount()}"
    
# In Python, built-in classes' names are in lowercase, but user-defined classes are in snake or camel case

# Object instantiation
b1 = Book('Book 1', 12, 'Author 1', 120)
b2 = Book('Book 2', 18, 'Author 2', 220)
b3 = Book('Book 3', 28, 'Author 3', 320)

# Python has special methods that are invoked only when certain conditions are met (they're usually named with 2 underscores
# at the start & end of the method name)
# For example, __repr__ can be used to display the book's information
# if __repr__ wasn't defined, printing the book objects would just give their class & memory location
#print(b1)
#print(b2)
#print(b3)

# Encapsulation
# add a private attribute to the book class to store the discount amount for a book
# trying to print the discount amount will not work because it is private, and it'll give an error message
# saying Book has no attribute __discount
#print("Title: %s\nQuantity: %d\nAuthor: %s\nPrice: $%.2f USD" % (b1.title, b1.quantity, b1.author, b1.price))

# the solution is to use getter & setter methods to access those private attributes
single_book = Book('Two States', 1, 'Chetan Bhagat', 200)
bulk_books = Book('Two States', 25, 'Chetan Bhagat', 200)
bulk_books.set_discount(0.20)

#print("Single Book Price: $%.2f USD\n" % single_book.get_price())
#print("Bulk Book Price: $%.2f USD\n" % bulk_books.get_price())
#print(single_book)
#print(bulk_books)

# Inheritance
# add the Novel and Academic classes so that they inherit from Book and add their own specific attributes (and/or methods)
class Novel(Book):
    def __init__(self, title, quantity, author, price, pages):
        super().__init__(title, quantity, author, price)
        self.__pages = pages
    
    # Pages getter/setter
    def get_pages(self):
        return self.__pages
    
    def set_pages(self, pages):
        self.__pages = pages
        
    # Novel-specific info display method
    def __repr__(self):
        return f"Title: {self.get_title()}, Quantity: {self.get_quantity()}, Author: {self.get_author()}, Price: {self.get_price()}, Discount: {self.get_discount()}, Number of pages: {self.get_pages()}"
    
class Academic(Book):
    def __init__(self, title, quantity, author, price, branch):
        super().__init__(title, quantity, author, price)
        self.__branch = branch
        
    # Branch getter/setter
    def get_branch(self):
        return self.__branch
    
    def set_branch(self, branch):
        self.__branch = branch
    
    # Academic-specific info display method
    def __repr__(self):
        return f"Title: {self.get_title()}, Quantity: {self.get_quantity()}, Author: {self.get_author()}, Price: {self.get_price()}, Discount: {self.get_discount()}, Branch: {self.get_branch()}"
    
n1 = Novel('Two States', 20, 'Chetan Bhagat', 200, 187)
n1.set_discount(0.20)
a1 = Academic('Python Foundations', 12, 'PSF', 655, 'IT')
print(n1)
print(a1)

# Polymorphism - a subclass' ability to adapt a method that already exists in the superclass to suit its own needs
# that is, a subclass can use a method as is from its superclass or modify that method as needed
# For example, the Novel and Academic classes can either use Book's version of __repr__ or
# have their own versions defined (per their own needs)

# Abstraction - not directly supported in Python -> have to make use of the package abc & the imports ABC & abstractmethod
# if an abstract method is defined in a superclass, subclasses that inherit from that superclass are required
# to have their own implementation/version of the method(s) marked as abstract
