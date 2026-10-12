#########################################
# Functions & Exception Handling
##########################################

import random

def add_numbers(a, b):
    result = a + b
    return result

total = add_numbers(5, 3)
print("Total:", total)

############ practice examples ###########

def square_number(num):
    return num ** 2

for i in range (3):
    no = random.randint(1,100)
    print ("Square of", no, ":", square_number(no))


def greet(name):
    return "Hello, " + name + "!" + " Welcome to the session."

print (greet("Ali"))

def asterik (no):

    for i in range(no):
        for j in range (i+1):
             print ('*', end = "")
        print()
        
asterik (5)

##########################################
# Scope of the Function (Local & Global)
##########################################

x = 10

def my_func():
    y = 5
    print (x + y)

my_func()

############ practice examples ###########

var = 'Ali'

def name():

    greeting = 'Hello'
    return f"{greeting} {var}"

print(name())

print (greeting)

##########################################
# Lambda Expressions
##########################################

square = lambda x: x * x
print (square(5))

add  = lambda a,b: a+b
print (add(3,5))

############ practice examples ###########

multiplication = lambda X,y : X * y

for i in range (2):
    no1 = random.randint(1,10)
    no2 = random.randint(1,10)
    print('no 1:',no1,"no 2:",no2)
    print (multiplication(no1,no2))


is_even = lambda x : x % 2 == 0 
print (is_even(2))

##########################################
# Map & Filter
##########################################

# map () applies a function to every item in a list, producing a new list
# filter() keeps onlt the items that satisfy a condition (return true)
# Both are often combined with lambdas for short, powerful one-liners.  
# map(function, iterable)                                 
"""In Python, map() and filter() are built-in, higher-order functions used to process and transform data collections (like lists, tuples, or sets)
without using explicit for loops. Both functions are "lazy"—they return iterator objects (map or filter objects) rather than fully evaluated lists, 
which helps save memory."""

# nums = [1, 2, 3, 4, 5]
nums = (1, 2, 3, 5, 7)
 
squared = list(map(lambda x: x*x, nums)) 
print (squared)

evens = list(filter(lambda x: x % 2 == 0, nums)) 
print (evens)

############ practice examples ###########

temp_celsius = [29,35,40,45,25]
convert_temp = list(map(lambda x: ((x*9/5)+32), temp_celsius))
print (convert_temp)


nums = [1,5,7,8,25,67,99]
check_no = list (filter(lambda x: x > 10,nums))
print (check_no)

##########################################
# Inner / Nested Functions
##########################################


############ practice examples ###########

def process_order (items):

    def order_print ():

        print ("\n *** Order Processed Items: ***\n")

        for item,price in items.items():
            print (f"* {item} : Rs {price}")
            print(f"The 10% discounted price for {item} is : Rs {round (price * 0.9) } \n")

    return order_print()
    
process_order({'Laptop':100000, 'Mouse':200, 'Keyboard':500})


##########################################
# File Handling
##########################################

with open ('notes.txt', 'w') as f:
    f.write('Helo AI class \n')

with open ('notes.txt', 'a') as f:
    f.write('Helo Shamaz \n')

with open ('notes.txt', 'r') as f:
    content = f.read()
    print (content)

############ practice examples ###########

with open ('subject names.txt', 'w') as file:
    pass

for i in range (3):
    user_input = input ("Enter your subject name: ")

    with open ('subject names.txt', 'a') as f:
        f.write (f"{user_input} \n")

with open ('subject names.txt', 'r+') as rw:
    print(rw.read())

    

