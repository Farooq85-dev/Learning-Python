# Object DataType or Data Type

# string
# integer (number)
# float point numbers (number)
# list
# tuple
# dict
# Boolean


# 1) String
str = "Farooq" # string
str = 'Farooq' # string
print(type(str)) # string

# 2) integer also number
num = 21
print(type(num)) # integer

# 3) float
flt = 2.34 # float
print(type(flt)) # float

# 4) list
lst = ["a", 2, 2.3, True] # many datatype of list
lst = [2, 2] # one datatype but alos list list
print(type(lst)) # list

# 5) tuple
tup = (1,2,3)
print(type(tup)) # tuple

# 6) dict
students  = {
    "userName":"Farooq",
    "className":"11th",
    "section":"A+"
}
print(type(students)) # dict
print(students["userName"]) 
print(students) # whole dictionary like object in javascript.

# 7) Boolean
bt = True
bf = False
print(type(bt)) # Boolean
print(type(bf)) # Boolean


# Mutable vs Immutable Data Types
# mutable and immutable refers to memory refernce.
# For Example:- 
x = 2
y = x
x = 10
print(y) # 2
print(x) # 10
print(y) # 2

# Mutable

# list 
# set
# dict
# array
# bytearray

# Immutable

# integers 
# string 
# floating point numbers
# Boolean
# Tuple
# Frzen set
# Bytes 
