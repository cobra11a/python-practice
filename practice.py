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

class Animal:
    def eat(self):
        print("Eating ")
    def sleep(self):
        print("sleeping")
class Dog(Animal):
    def bark(self):
        print("woof!")
d=Dog()
d.sleep()
d.eat()




























