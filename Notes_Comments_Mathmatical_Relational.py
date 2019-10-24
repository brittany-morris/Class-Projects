# Brittany Morris
# Python 2.7 (SSF1910)
# Notes: Comments, Mathematical and Relational Operators in Python



# This is a comment

# Inline Comment
mything = "Apples" # My thing is a kind of fruit

# Multi Line Comment
'''
This is how you write a multi line comment.
There is more than one line available and you can make it
as large or small as you need it to be.
'''

##########################
# Project: No real name  #
# Version: 0.1           #
##########################



# Mathematical Operators

# Addition          +
# Subtraction       -
# Multiplication    *
# Division          /
# Exponents         **
# Modulus           % (Remainder after dividing two numbers)

x = 5
y = 12.95
z = 0x31EBBC3
zz = 3.14j

print x + y
print y - x
print x * y
print y / x
print x ** y
print x % y
print y % x



# Relational Operators
# Less Than: <
# Less than or Equal to: <=
# Greater Than: >
# Greater Than or Equal to: >=
# Equal to: ==
# Not Equal: !=

age = input("Enter Age: ")
credit_card = False

if age >= 25 and credit_card == True:
    result = "You are old enough to rent a car."
elif age >= 25 and credit_card == False:
    result = "You are old enough to rent a car but do not have a credit card."
elif age >= 21 or credit_card == True:
    result = "You are not old enough to rent a car but you are old enough to shop online."
elif age >= 18:
    result = "You are old enough to vote, but not rent a car."
else:
    result = "You're too young to do anything."

print result