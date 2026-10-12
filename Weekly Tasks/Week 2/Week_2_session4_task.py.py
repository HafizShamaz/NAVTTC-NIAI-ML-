#########################################
# Ternaery (Conditional) expression
#########################################

age = 20
status = "Adult" if age >= 18 else "Minor"
print(status)


########### practice examples ###########
no = 10
check = "even" if no%2 == 0 else "odd"
print(check)


marks = 40
result = "Pass" if marks >= 40 else "Fail"
print (result)

#########################################
# Break , Contine, Pass
#########################################

for i in range(10):

    if i ==5:
        break
    print (i)

for i in range(6):
    if i%2 == 0:
        continue
    print (i)


########### practice examples ###########

for i in range(20):
    if i == 15:
        break
    print (i)

for i in range (20):

    if i % 3 == 0:
        continue
    print (i)

#########################################
# For Loop & Enumerate
#########################################

fruits= ["apple", "banana", "cherry", "kiwi", "mango"]

for fruit in fruits:
    print(fruit)

for index, fruit in enumerate(fruits): # enumerate gives us both list index and value
    print (index, fruit)

######### Practice examples ###########

favourite_fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

for index, favourite_fruit in enumerate (favourite_fruits):
    print(index, favourite_fruit)


for i in range(1,11): 
    print (i ** 2)


#########################################
# While Loop
#########################################

count = 0
while count < 5:
    print(count)
    count += 1

######### Practice examples ###########

count = 0
while count < 20:
    if count % 2 == 0:
        print(count)
    count += 1

count = 10
while count > 0:
    print(count)
    count -= 1

#########################################
# Nested Loops
#########################################

for i in range(1, 4):
    for j in range(1, 4):
        print(i,"x",j,"=",i*j)

######### Practice examples ###########

for i in range(5):
    for j in range(5):
        print (i, "x",j, "=", i*j)

## Same example multiple code ###
for i in range (6):
    for j in range (i):
        print (i * "*")
        break

for i in range (6):
    for j in range (i):
        print ("*", end = "")
    print ()
################

for i in range (6):
    for j in range (i):
        print ("*", end = "")
    print ()
