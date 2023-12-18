#!/usr/bin/env python
# coding: utf-8

# In[1]:


from abc import ABC, abstractmethod
class Car(ABC):
  def mileage(self):
    pass
class Tesla(Car):
  def mileage(self):    
    print("The mileage is 30kmpl")
class Suzuki(Car):
  def mileage(self):
    print("The mileage is 25kmpl")
class Duster(Car):
  def mileage(self):
    print("The mileage is 24kmpl")
class Renault(Car):
  def mileage(self):
    print("The mileage is 27kmpl")    

t=Tesla()
t.mileage()

s=Suzuki()
s.mileage()

d=Duster()
d.mileage()


# In[2]:


from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius**2
    
    def perimeter(self):
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)

class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
    
    def area(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))
    
    def perimeter(self):
        return self.side1 + self.side2 + self.side3

# Creating instances of shapes
circle = Circle(5)
rectangle = Rectangle(4, 6)
triangle = Triangle(3, 4, 5)

# Calculating and displaying results
print(f"Circle - Area: {circle.area()}, Perimeter: {circle.perimeter()}")
print(f"Rectangle - Area: {rectangle.area()}, Perimeter: {rectangle.perimeter()}")
print(f"Triangle - Area: {triangle.area()}, Perimeter: {triangle.perimeter()}")


# In[3]:


from abc import ABC, abstractmethod

class LibraryItem(ABC):
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.checked_out = False

    @abstractmethod
    def display_details(self):
        pass

    def check_out(self):
        if not self.checked_out:
            self.checked_out = True
            print(f"{self.title} by {self.author} has been checked out.")
        else:
            print(f"{self.title} by {self.author} is already checked out.")

    def return_item(self):
        if self.checked_out:
            self.checked_out = False
            print(f"{self.title} by {self.author} has been returned.")
        else:
            print(f"{self.title} by {self.author} is already in the library.")


class Book(LibraryItem):
    def __init__(self, title, author, pages):
        super().__init__(title, author)
        self.pages = pages

    def display_details(self):
        print(f"Book Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Pages: {self.pages}")


class DVD(LibraryItem):
    def __init__(self, title, director, duration):
        super().__init__(title, director)
        self.director = director
        self.duration = duration

    def display_details(self):
        print(f"DVD Title: {self.title}")
        print(f"Director: {self.director}")
        print(f"Duration: {self.duration} minutes")


class LibraryMember:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.checked_out_items = []

    def check_out_item(self, item):
        if not item.checked_out:
            item.check_out()
            self.checked_out_items.append(item)
        else:
            print("This item is already checked out.")

    def return_item(self, item):
        if item in self.checked_out_items:
            item.return_item()
            self.checked_out_items.remove(item)
        else:
            print("You haven't checked out this item.")

    def display_checked_out_items(self):
        if self.checked_out_items:
            print(f"{self.name}'s Checked Out Items:")
            for item in self.checked_out_items:
                print(f"- {item.title} by {item.author}")
        else:
            print(f"{self.name} hasn't checked out any items.")


# Example Usage:

book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
dvd1 = DVD("Inception", "Christopher Nolan", 148)

member1 = LibraryMember("Alice", 101)
member2 = LibraryMember("Bob", 102)

member1.check_out_item(book1)
member2.check_out_item(book1)  # Trying to check out the same book
member2.check_out_item(dvd1)

member1.display_checked_out_items()
member2.display_checked_out_items()

member1.return_item(book1)
member2.return_item(dvd1)

member1.display_checked_out_items()
member2.display_checked_out_items()


# In[4]:


from abc import ABC, abstractmethod

# Abstract Product class
class Product(ABC):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @abstractmethod
    def display_info(self):
        pass

# Derived classes for different product types
class ElectronicProduct(Product):
    def __init__(self, name, price, warranty_period):
        super().__init__(name, price)
        self.warranty_period = warranty_period

    def display_info(self):
        print(f"{self.name} - ${self.price} (Warranty: {self.warranty_period} months)")

class ClothingProduct(Product):
    def __init__(self, name, price, size):
        super().__init__(name, price)
        self.size = size

    def display_info(self):
        print(f"{self.name} - ${self.price} (Size: {self.size})")

# Abstract Cart class
class Cart(ABC):
    def __init__(self):
        self.items = []

    @abstractmethod
    def add_to_cart(self, product):
        pass

    @abstractmethod
    def remove_from_cart(self, product):
        pass

    @abstractmethod
    def view_cart(self):
        pass

# Derived class for a basic shopping cart
class ShoppingCart(Cart):
    def add_to_cart(self, product):
        self.items.append(product)
        print(f"{product.name} added to the cart.")

    def remove_from_cart(self, product):
        if product in self.items:
            self.items.remove(product)
            print(f"{product.name} removed from the cart.")
        else:
            print(f"{product.name} not found in the cart.")

    def view_cart(self):
        print("Shopping Cart:")
        total_price = 0
        for item in self.items:
            item.display_info()
            total_price += item.price
        print(f"Total Price: ${total_price}")

# Example usage
if __name__ == "__main__":
    laptop = ElectronicProduct("Laptop", 1200, 12)
    t_shirt = ClothingProduct("T-Shirt", 20, "M")

    cart = ShoppingCart()
    cart.add_to_cart(laptop)
    cart.add_to_cart(t_shirt)

    cart.view_cart()

    cart.remove_from_cart(laptop)
    cart.view_cart()


# In[5]:


from abc import ABC, abstractmethod

# Abstract Investment class
class Investment(ABC):
    def __init__(self, symbol, quantity, price_per_unit):
        self.symbol = symbol
        self.quantity = quantity
        self.price_per_unit = price_per_unit

    @abstractmethod
    def calculate_value(self):
        pass

# Derived classes for various types of investments
class Stock(Investment):
    def calculate_value(self):
        return self.quantity * self.price_per_unit

class Bond(Investment):
    def calculate_value(self):
        return self.quantity * self.price_per_unit

class RealEstate(Investment):
    def __init__(self, address, quantity, price_per_unit):
        super().__init__("Real Estate", quantity, price_per_unit)
        self.address = address

    def calculate_value(self):
        return self.quantity * self.price_per_unit

# Abstract Portfolio class
class Portfolio(ABC):
    def __init__(self):
        self.investments = []

    @abstractmethod
    def add_investment(self, investment):
        pass

    @abstractmethod
    def calculate_portfolio_value(self):
        pass

# Derived class for a financial portfolio
class FinancialPortfolio(Portfolio):
    def add_investment(self, investment):
        self.investments.append(investment)

    def calculate_portfolio_value(self):
        total_value = 0
        for investment in self.investments:
            total_value += investment.calculate_value()
        return total_value

# Example usage
if __name__ == "__main__":
    stock1 = Stock("AAPL", 10, 150)
    bond1 = Bond("US Treasury Bond", 5, 1000)
    real_estate1 = RealEstate("123 Main St", 2, 500000)

    portfolio = FinancialPortfolio()
    portfolio.add_investment(stock1)
    portfolio.add_investment(bond1)
    portfolio.add_investment(real_estate1)

    total_portfolio_value = portfolio.calculate_portfolio_value()

    print(f"Total Portfolio Value: ${total_portfolio_value}")


# In[6]:


from abc import ABC, abstractmethod

class UserProfile(ABC):
    def __init__(self, username, email):
        self._username = username
        self._email = email
        self._posts = []

    @abstractmethod
    def post(self, content):
        pass

    @abstractmethod
    def comment(self, post_id, comment):
        pass

    @abstractmethod
    def like(self, post_id):
        pass

class RegularUser(UserProfile):
    def post(self, content):
        self._posts.append(content)
        print(f"Regular User {self._username} posted: {content}")

    def comment(self, post_id, comment):
        if post_id < len(self._posts):
            print(f"Regular User {self._username} commented on post {post_id}: {comment}")
        else:
            print("Invalid post ID")

    def like(self, post_id):
        if post_id < len(self._posts):
            print(f"Regular User {self._username} liked post {post_id}")
        else:
            print("Invalid post ID")

class Admin(UserProfile):
    def post(self, content):
        self._posts.append(content)
        print(f"Admin {self._username} posted: {content}")

    def comment(self, post_id, comment):
        if post_id < len(self._posts):
            print(f"Admin {self._username} commented on post {post_id}: {comment}")
        else:
            print("Invalid post ID")

    def like(self, post_id):
        if post_id < len(self._posts):
            print(f"Admin {self._username} liked post {post_id}")
        else:
            print("Invalid post ID")

# Example usage:

regular_user = RegularUser("Alice", "alice@example.com")
admin_user = Admin("Admin1", "admin@example.com")

regular_user.post("Hello, this is my first post!")
admin_user.post("Welcome to our new platform!")

regular_user.comment(0, "Nice post!")
admin_user.comment(1, "Great to have you here.")

regular_user.like(1)
admin_user.like(0)


# In[7]:


from abc import ABC, abstractmethod

class Product(ABC):
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    @abstractmethod
    def display_info(self):
        pass

class Electronics(Product):
    def __init__(self, name, price, quantity, brand):
        super().__init__(name, price, quantity)
        self.brand = brand

    def display_info(self):
        print(f"Electronics: {self.name} | Brand: {self.brand} | Price: ${self.price} | Quantity: {self.quantity}")

class Clothing(Product):
    def __init__(self, name, price, quantity, size):
        super().__init__(name, price, quantity)
        self.size = size

    def display_info(self):
        print(f"Clothing: {self.name} | Size: {self.size} | Price: ${self.price} | Quantity: {self.quantity}")

class Store(ABC):
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        print(f"Added {product.name} to the store inventory.")

    def display_inventory(self):
        print("Store Inventory:")
        for product in self.products:
            product.display_info()

# Example Usage:

store = Store()

tv = Electronics("TV", 500, 10, "Samsung")
shirt = Clothing("T-Shirt", 20, 50, "M")

store.add_product(tv)
store.add_product(shirt)


# In[ ]:




