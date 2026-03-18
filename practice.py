import os 
os.system('cls')

# Customized Greeting Based on Time of Day
# Create a variable user and assign the value 16

# Use if-elif-else statements to print:

# "Good Morning" if the hour is between 5 and 11,

# "Good Afternoon" if the hour is between 12 and 17,

# "Good Evening" if the hour is between 18 and 21,

# "Good Night" for all other hours.

# Print "Greeting code has completed."

# Expected Output:

# For input 10:

# Good Morning
# Greeting code has completed.
# For input 15:

# Good Afternoon
# Greeting code has completed.

# hour = 16

# if 5 <= hour <= 11:
#     print("Good Morning")
# elif 12 <= hour <= 17:
#     print("Good Afternoon")

# class Animal :
#     def Dog (self):
#         print("Dog is a animal")

# a1=Animal()
# a1.Dog()

# class Car:
#     def __init__(self, brand, color):
#         self.brand = brand
#         self.color = color
        

# c1 = Car("BMW", "Red")

# print(c1.brand," , " , c1.color)



# class student:
#     def __init__(self, name , age: int):
#         self.name = name 
#         self.age = int(age) 
     


# s1 = student ("Sudhanshu" , 23)
# print(s1.name , s1.age)


# Inheritance 

# class Animal:
#     def eat(self):
#         print("Eating ")
#     def sleep(self):
#         print("sleeping")
# class Dog(Animal):
#     def bark(self):
#         print("woof!")
# d=Dog()
# d.sleep()
# d.eat()



# class Book:
#     def __init__(self ,title,price):
#         self.title = title
#         self.price = price
    
#     def show_details(self):
#         print("Book Title:" ,self.title)
#         print("Price" ,self.price)

# b1 = Book("Python Basics" , 500)
# b1.show_details()

# Read using python

# with open ("practice.txt" , "r") as file :
#     content = file.read()
#     print(content)

# Writing data using python

# file = open("practice.txt" ,"w")
# file.write("Hellloolo\n")
# file.close()

# with open("practice.txt" ,"w") as file :
#     file.write("Hello guys\n")
#     file.write("Hello guyyys")


# try and except 


ItemsInCart = 0

def add_to_cart(items_to_add):
    global ItemsInCart

    # Check negative items
    if items_to_add < 0:
        raise Exception("Cannot add a negative number of items.")
    
    # Check cart limit
    if ItemsInCart + items_to_add > 5:
        raise Exception("Cart limit exceeded.")
    
    # Add items
    ItemsInCart = ItemsInCart + items_to_add
    print(f"{items_to_add} items added. Total in cart: {ItemsInCart}")


# Example usage
try:
    add_to_cart(-5)   # valid
     # should raise exception
except Exception as e:
    print(e)



TicketBooked = 0 
 
def book_ticket(tickets_to_book):
    global TicketBooked

    if tickets_to_book <0 :
        raise Exception("Cannot book negative tickets.")
    
    if  TicketBooked + tickets_to_book > 10 :
        raise Exception("Booking limit exceeded.")
    
    
    
    
try:
    book_ticket(4)
    book_ticket(-1)
    book_ticket(8)

except Exception as e:
    print(e)



































