# Brittany Morris
# Python 2.7 (SSF1910)
# Activity: Create a Code Name Generator

# Import the Random Module
# This module allows you to access a set of functions specifically used
# to generate random results.

import random

# Code Name Lists
alpha = ['Crimson', 'Phantom', 'Zephyr', 'Palisade', 'Skyfall', 'Borealis', 'Typhoon', 'Manifest']

omega = ['Whirlwind', 'Gatecrasher', 'Iceberg', 'Zealot', 'Element', 'Neon', 'Epoch', 'Dynasty']


for x in range(5):
     print "Operation: " + random.choice(alpha) + " " + random.choice(omega)
