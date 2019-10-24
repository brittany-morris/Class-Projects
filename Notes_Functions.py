# Brittany Morris
# Python 2.7 (SSF1910)
# Notes: Functions in Python

###############################
'''
# Functions in Python
# What is a Function? A small reuseable block of code

# Built in Functions / Methods

print ('This is the arguement')

number = 'Danny Tartabull, Outfielder, wears number # ' + str(45)
print number
print type(number)

print len(number)

print (number.upper())
print (number.lower())
print (number.title())

numbers = [4,6,123,295,0,12]
names = ['Adam', 'Ant', 'Aardvark', 'Banana']

print (sum(numbers))

# Sorted only works on lists and dictionaries not on Tuples
print (sorted(numbers))
print (sorted(names))

messy = "   I don't like to keep things even.   "

print messy.strip()



# Imported Module Methods
import random

print numbers
random.shuffle(numbers)
print numbers
print random.choice(numbers)

# Adding random.shuffle and random.choice together makes the choice even more random.



# Variable Scope within a Function

# Define a Custom Function
def printmessage(x):
    print x

# Assigning text to a variable
mymessage = raw_input('Enter message: ')

# Calling the function into action and passing it the variable
printmessage(mymessage)

printmessage("This is another bit of text I want to pass.")
printmessage(44)


# Define x
x = 'I am a meat popsicle.'


# Define Function
def squarethis(x):
    return x * x

mynumber = squarethis(3)

print x

print mynumber


def useglobal():
    global x
    print x

def localsonly(x):
    x = "local"
    print x

useglobal()
localsonly(x)
'''



# Creating Custom Function in Python

# Define a custom function

def printmessage(x):
    print x

# Assigning text to variable
mymessage = raw_input('Enter Message: ')

# Calling the function into action and passing it the variable.
printmessage(mymessage)

printmessage("This is another bit of text I want to pass.")
printmessage(44)
