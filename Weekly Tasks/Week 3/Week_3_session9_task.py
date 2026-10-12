##########################################
# Numpy Array
##########################################

import numpy as np

arr = np.array([1,2,3,4,5])
print (arr)

zeros = np.zeros ((2,3)) #2 rows and 3 coloumns
print (zeros)

rand= np.random.randint(1,10,3)
print(rand)


############ practice examples ###########

arr = np.array([9,8,7,6,5])
print (arr)

ones = np.ones ((3,3)) #2 rows and 3 coloumns
print (ones)

rand= np.random.randint(1,100,4)
print(rand)

##########################################
# Array Attributes (shape, dtype, size, ndim)
##########################################

a = np.array ([[1,2,3],[4,5,6]])

print (a.shape)
print(a.dtype)
print(a.size)
print(a.ndim)

############ practice examples ###########

a = np.array ([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print (a.shape)
print(a.dtype)
print(a.size)
print(a.ndim)

b = np.array ([[5,6,7,8],[1,2,3,4],[9,10,11,12]])

# b = np.array ([[1.1,2.2,3.3,4.4],[5.5,6.6,7.7,8.8],[9.8,10.10,11.11,12.12]])
print (b.shape)
print(b.dtype)
print(b.size)
print(b.ndim)

print(np.array_equal(b, a))  

##########################################
# Array methods (reshape,max/min, argmax,argmin)
##########################################

b = np.array ([3,7,1,9,4])

print (b.reshape(5,1))
print(b.max(),b.min())
print(b.argmax(),b.argmin())

############ practice examples ###########

b = np.array ([3,7,0,10,4,8])
print (b.reshape(6,1))
print(b.max(),b.min())

c = np.array ([56,1,5,10,3,100,56,0]) 
print(c.argmax(),c.argmin())

##########################################
# Copying, Appending, Inserting
##########################################

c = np.array ([1,2,3])

c_copy = c.copy()
c_copy[0] = 99
print (c,c_copy)

d = np.array([1,2,3])
print (np.append(d,[4,5])) # insert add element at the end of the array
print (np.insert(d,1,100)) # 1 is a position

############ practice examples ###########

c = np.array ([100,101,102])
c_copy = c.copy()
c_copy[0] = 99
print (c,c_copy)

d = np.array([151,152,153])
print (np.append(d,[4,5,8])) 
print (np.insert(d,2,100)) 

##########################################
# Sorting, deleting, Combining, Splitting
##########################################

e = np.array ([5,2,8,1])
print(np.sort(e))
print(np.delete(e,0))

f1,f2 = np.array([1,2]),np.array([3,4])
print(np.concatenate((f1,f2)))
print (np.array_split(np.arange(1,7),3))

############ practice examples ###########

e = np.array ([5,2,8,1,10,20])
print(np.sort(e))
print(np.delete(e,2))

arr1,arr2 = np.array([1,2,3]),np.array([4,5,6])
result = np.concatenate((arr1,arr2))
print (np.array_split(result,2))


##########################################
# Indexing, Broadcasting & ArrayMath
##########################################

arr = np.array([1,2,3,4])

np.save("my_array.npy", arr)

loaded = np.load("my_array.npy")
print(loaded)

##########################################
# Indexing & Selection (2D,Logical)
##########################################

g = np.array ([[1,2,3],[4,5,6],[7,8,9]])

print (g[1,2]) # row 1 and coloumn 2
print(g[g>5])


############ practice examples ###########

g = np.array ([[1,2,3],[4,5,6],[7,8,9]])

print (g[2,1]) # row 1 and coloumn 2
print(g[g%2==0])

##########################################
# Broadcasting
##########################################

h= np.array ([1,2,3])
print (h +10) # 10 is broadcasted to all

############ practice examples ###########

h= np.array ([1,2,3,4,5])
print (h +100) # 10 is broadcasted to all
print(((h*3)-1))

##########################################
# Type Casting & Arithmatic Operations
##########################################

i = np.array ([1.5,2.7,3.1])
print (i.astype(int)) #truncate decimals

j = np.array ([1,2,3])
k = np.array ([4,5,6])

print (j+k, j-k, j*k)
print (j/k, j**2)

############ practice examples ###########

i = np.array ([3.5,6.7,9.1])
print (i.astype(int)) #truncate decimals

j = np.array ([10,20,30,40])
k = np.array ([5,6,7,8])

print (j+k, j-k, j*k)
print (j/k, j**2)

##########################################
# Universal Array Functions (sqrt,exp,sin,etc)
##########################################

m = np.array ([1,4,9,16])
print (np.sqrt(m))

n = np.array([1,2])
print(np.exp(n))

############ practice examples ###########

m = np.array ([4,9,16,32,64])
print (np.sqrt(m))

angles = np.array([60,90,180,360])
print(np.sin(angles))
