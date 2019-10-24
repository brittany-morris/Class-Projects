# Brittany Morris
# Python 2.7 (SSF1910)
# Notes: Comments, Mathematical and Relational Operators in Python

# STRINGS
mystring = 'This is a string'
mystring = "This is also a string"
mystring = """This is a multiple line string
that we can type all sorts of nonsense into
and it doesn't even matter"""

price = 12.75
item = 'Sweater'

print("This " + item + " costs $" + str(price))



# String Methods
thing = "AdVeNtUrE"

print thing
print thing.upper()
print thing.lower()
print thing.title()

print 'This is a single quote'
print "This is a double quote"
print '''This is a multi line comment.'''

# Using raw_input()         --Used in 2.x branch
name = raw_input('Please enter name: ')
print name

# Using input()            --Use in 3.x branch
mileage = input('Please enter mileage: ')

