##################################
#Lists
###################################

fruits = ["apple", "banana", "mango"]

fruits.append("orange")
fruits.remove("banana")

print (fruits[0])
print (fruits[-1])
print (len(fruits))

cities = []
for i in range (5):
    user_input = input ("Enter 5 cities of your choice: ")
    cities.append(user_input)


print (cities)

cities.append(input("Enter one more city of your choice: "))
print (cities)
cities.remove(input("Remove one of your choice: "))

print (cities[1])
print (cities[-1])
print (len(cities))


###################################
#Tuples
###################################


colors = (200,150,255)
print (colors[0:3])
print (len(colors))

###################################
#Dictionaries
###################################

 
student = {
    "name": "Ali",
    "age": 30,
}

print (student["name"])
student["age"] = 31
student["city"] = "Karachi"

for key,value in student.items():
    print (key, ":", value)


book = {
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald",
    "year": 1995,}


for key,values in book.items():
    print (key, ":", values)

book ["year"] = "2026"

for key,values in book.items():
    print (key, ":", values)


###################################
#Sets
###################################


nums = {1, 4, 5, 3, 2}

print (nums)
nums.add(6)
nums.remove(1)
print (3 in nums)

nums = [1,2,3,4,5,5,4,3,2,1]
print (nums)

# num = set(nums)
num = {*nums}
# # num = {1,2,3,4,5,5,4,3,2,1}
print (num)
print (2 in num)

###################################
#Conditions
###################################


marks = 75

if marks >= 90:
    print ("A+")
elif marks >= 70:
    print ("B")
else:
    print("Fail" )

marks = 75

if marks >= 90:
    print ("A+")
elif marks >= 80:
    print ("B+")
elif marks >= 70:
    print("C+")
else:
    print("Fail" )

age = int(input("Enter your age: "))
has_ticket = True

if age >= 18 and has_ticket == True:
    print("You can enter the concert!")
else:
    print("You cannot enter the concert.")


