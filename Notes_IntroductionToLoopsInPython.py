# Brittany Morris
# Python 2.7 (SSF1910)
# Lesson: Introduction to Loops in Python

### Loops in Python ###
'''
FOR Loops- Typically used to iterate through an array or in conjunction with a
built-in Python function like xrange() to execute a specific number of times.

WHILE Loops- Used to run a specific set of instructions while a specific condition
exists - usually True or False. You can also use values stored in a variable to set
the conditions under which a WHILE Loop will run.
'''

# For Loops
for x in range(0, 20):
    print (x)

for x in range(10):
    if x == 5:
        print(x)
        print "You've landed a 5!"
        continue
    print(x)

for x in range(10):
    if x == 5:
        print(x)
        print "You've landed a 5!"
        break
    print(x)

# for x in xrange(start, stop, step)
# step is the number you are counting by
for x in xrange(1,22):
    print (x)
    if x >= 17 and x < 21:
        print("Close but no cigar!")
        continue
    elif x == 21:
        print ("Blackjack!")



# Using FOR loops in Python
colors = ['red', 'white', 'blue']

for color in colors:
    print color

print colors

for x in xrange(0, 100, 5):
    print x



# Using WHILE Loops in Python
# a set of instructions that runs continuously until a certain thing is met
# .strip removes the white space
while True:
    n =  raw_input("Enter 'hi': ")
    if n.strip() == 'hi':
        print "Hello"
        break
