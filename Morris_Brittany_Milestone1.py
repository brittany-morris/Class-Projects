# Brittany Morris
# Python 2.7 (SSD1910)
# Milestone 1

# ADD YOUR MULTI LINE COMMENT HERE
'''
Here is my multi line comment.
This file will be a play on rock, paper, scissors
'''

# Import the random Module
import random

# Here are your list of Pirates
pirates = [
    'Captain William Kidd',
    'Pierre Le Grand',
    'Red Leg Grieves',
    'Edward Low',
    'Calico Jack Rackham',
    'Anne Bonny',
    'Captain Henry Morgan',
    'Black Sam Bellamy',
    'Black Bart Roberts',
    'Edward Blackbeard Teach']

# PRINT THE CONTENT OF THE PIRATES LIST TO THE SCREEN HERE
print " "
print "Pirates:"
for x in pirates:
    print(x)

#  Attacks List
attack = ['dodge', 'parry', 'thrust']

# PRINT THE CONTENTS OF THE ATTACK LIST TO THE SCREEN HERE
print " "
print "Attacks:"
for y in attack:
    print(y)

# Choosing the Characters for the fight
player = random.choice(pirates)
opponent = random.choice(pirates)


# #############################################################################
# Change the line below to correctly concatenate PLAYER and OPPONENT with
# the variables above so that when the statement prints to screen, the chosen
# character names are shown.
# #############################################################################

print " "
print "Ahoy ye swabs! Prepare for battle!"
print player + " has challenged " + opponent + " in one on one combat!"

# Choosing the attack
pattack = random.choice(attack)
oattack = random.choice(attack)


# CREATE A CORRECTLY CONCATENATED STRING THAT CONTAINS PLAYER, OPPONENT, PATTACK & OA
print " "
print player + ' throws the attack of ' + pattack
print opponent + 'throws the attack of '+ oattack

# Dodge beats Parry > Parry beats Thrust > Thrust beats Dodge

"dodge" > "parry"
"parry" > "thrust"
"thrust" > "dodge"


parry = "attackp"
dodge = "attackd"
thrust = "attackt"

print " "

if pattack == oattack:
    print ('Tie!')
elif pattack > oattack:
    print ("The Winner is " + player + "!")
elif pattack < oattack:
    print ("The Winner is " + opponent + "!")


