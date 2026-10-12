##########################################
# Exception Handling
##########################################

try:
    num = int(input("Enter a number: "))
    print (round(10/num))

except ZeroDivisionError:
    print ("Can not divide by zero!")

except ValueError:
    print ("This is not a valid number!")

finally:
    print ("Done Trying")

############ practice examples ###########

try:
    num1 = int(input("Enter 1st number: "))
    num2 = int(input("Enter 2nd number: "))
    print (round(num1/num2))

except ZeroDivisionError:
    print ("Can not divide by zero!")

except ValueError:
    print ("Please write numeric number to get required answer!")

##########################################
# OOP in Python
##########################################

class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def greet(self):

        print(f"Hi, I am {self.name}")

s1 = Student("Ali", 20)
s1.greet()


############ practice examples ###########

class car:

    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def description(self):

        print (f"Car brand is {self.brand} and the manufacturing year is {self.year}")

obj = car ("Toyota Corolla", 2026)
obj.description()

obj = car ("Honda Civic", 2021)
obj.description()

##########################################
# Instance vs Class Variables & Methods
##########################################

class student:

    school = "NAVTTC" # class variable

    def __init__(self, name):
        self.name = name # instance variable

s1 = student("Ali")
s2 = student("Shamaz")

print(s1.school,s2.school)
print(s1.name)

############ practice examples ###########

class employee:

    company = "Netsol" # class variable

    def __init__(self, name):
        self.name = name # instance variable

e1 = employee("Ali")
e2 = employee("Shamaz")
e3 = employee("Hamad")

my_obj = [e1,e2,e3]
for obj in my_obj:
    print (f"{obj.name} works in {obj.company}")

##########################################
# Constructor & Destructor
##########################################

class student:

    def __init__(self, name):
        self.name = name # instance variable
        print (f"{self.name} created")


    def __del__(self):
        print (f"{self.name} destroyed")

s1 = student("Ali")
del s1

############ practice examples ###########

class Book:

    def __init__(self, title):
        self.title = title # instance variable
        print (f"Book added with the title: {self.title}")

    def __del__(self):
        print (f"Book removed with the title: {self.title}")

b1 = Book("Rich Dad Poor Dad")
del b1

##########################################
# Inheritance (Single, Multilevel, Hierarchical)
##########################################

class Animal:
    def eat(self):
        print("Eating ...")

class Dog(Animal): #single inheritance
    def bark(self):
        print("Barking...")

d = Dog()
d.eat() # inherited
d.bark()

############ practice examples ###########

class Vehicle:
    def start(self):
        print("Starting")

class car(Vehicle): #single inheritance
    def honk(self):
        print("peep")

v = Vehicle()
v.start() # inherited
v.honk()

########

class Shape:
    def __init__(self):
        pass

class Circle(Shape):
    pass

class Square(Shape):
    pass

s = Shape()

##########################################
# Multiple Inheritance & MRO (Method Resolution Order)
##########################################

# MRO (Method Resolution Order) decides which parent's method runs first if there's a conflict

class Flyer:
    def move(self):
        print('Flying')

class Swimmer:
    def move(self):
        print('Swimming')

class Duck(Flyer, Swimmer):  # multiple
    def quack(self):
        print( "Quack quack!" )

donald = Duck()

print (Duck.__mro__)
donald.quack()
donald.move()  # uses Flyer first
Swimmer.move(donald) # explicit way to call a specific parent method

############ practice examples ###########

class Camera:
    def features (self):
        print ("Camera features")

class Phone:
    def features (self):
        print ("Phone features")

class Smartphone (Camera, Phone):
    pass

sm = Smartphone()
sm.features()
Phone.features(sm)
print(Smartphone.__mro__)


##########################################
# Access Specifiers & Name Mangling
##########################################

class Account:
    def __init__(self, balance):
        self.balance = balance       # public
        self._pin = 1234             # protected
        self.__password = 'secret'   # private

a = Account(500)
print(a.balance)
print(a._pin)
print(a.__password)  #→ Error!

############ practice examples ###########

class BankAccount:

    def __init__(self,account_holder = 'Ali'):

        self.account_holder = account_holder # Public
        self._branch = 'Muslim Town' # Protected
        self.__pin = 1234 #private


bank = BankAccount('Hafiz Shamaz') # public variable can be overwrite 
print (bank.account_holder) 

bank.branch = 'abd' # protected variable can not be overwrite outside the class
print (bank._branch)
# print (bank.__pin) # private variable not callable outside the class only use within the class


##########################################
# Inner Classes, Association, Aggregation & Composition
##########################################

class Engine:
    def start(self):
        print('Engine started')

class Car:
    def __init__(self):
        self.engine = Engine()  # composition

    def drive(self):
        self.engine.start()

Car().drive()


############ practice examples ###########

class Library:

    def record (self):

        print ("We have the books of every topic")

class Book:

    def __init__(self):
        self.library = Library() # composition
    
    def re (self):

        self.library.record()