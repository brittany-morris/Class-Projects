# Brittany Morris
# Python 2.7 (SSF1910)
# Lesson: Delimiters, Conditional Statements and Flow Control


# Script Organization: Python Delimiters

name = "Slim Shady"

# Conditional Statement
if name == "Slim Shady":
    print "Please Stand Up."
else:
    print "Please sit down"

# Simple Loop
for x in xrange(10):
    print x

# Custom Function
def athing():
    print "This is a custom function"



# Conditional Statements and Flow Control
'''
if this condition exist:
    do this set of instructions
elif this condition exists
    do this set of instructions instead
'''

# If/ THEN / Else
# if / elif / else

age = input("Enter Age: ")

if age >= 25:
    result = "You are old enough to rent a car."
elif age >=21:
    result = "You are not old enough to rent a car but you are old enough to vote."
elif age >= 18:
    result = "You are old enough to vote, but you can not rent a car."
else:
    result = "You're too young to do anything."

print result