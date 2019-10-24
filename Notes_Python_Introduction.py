# Brittany Morris
# Python 2.7 (SSF1910)
# Activity: Exploring PyCharm

# This is a comment

# Data Types in Python
# 5 Data Types - Strings, Numbers, Tuples, Dictionaries



# Strings - Text encapsulated by quotes

# Single Quote
print 'Hello World'

# Double Quote String
print "Hello World"

# Mixed Quote String
# Do not mix " with ' or you will get an error

# Triple Quotes (Used when you need to enter a lot data)
print '''
A whole lot of data inside on little string
It doesn't matter how much or if it is on more than 
one line because it is a multi line string.
'''



# Numbers

# Integer (Full number no decimals)
x = 5

# Floating Point (A number with decimals place)
y = 12.95

# Long integer (A number of unlimited size)
# 52 345 795
z = 0x31EBBC3

# Complex number (Numbers that deal with real and imaginary components)
zz = 3.14j



# Booleans (True or False statements)

in_stock = True
back_order = False



# Arrays (multi-dimensional variables that can store multiple levels of data by referencing a single variable.

# List []
shopping_cart = ['wireless mouse', 'lcd screen cleanrer', 'cat food', 'funions']
cart_cost = [14.99, 4.99, 45.99, 3.99]

print shopping_cart[0]

# Tuple () This is a multiple data type container
item = ('Sweater', 29.95, ['small', 'medium', 'large'], True)

# Dictionaries {} - key : value
pets = {'Lana' : 'cat' , 'Leela' : 'cat'}



# Variables (Container that stores the information)
naMe = "Joe"
Name = "Jim"
NAME = "Dolores"
namE = "Vanessa"

print naMe
print Name
print NAME
print namE



# Using Raw_Input()
name = raw_input('Please enter name: ')
name = input('Please enter name: ')
print name