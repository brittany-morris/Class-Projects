# Brittany Morris
# Python 2.7 (SSF1910
#I am Groot

import random

def randomator (L):
    random.shuffle(L)
    return random.choice(L)

def importer(T):
    with open (T, 'r') as f:
        return f.read().splitlines()

# ---------------------------------

# List Characters
characters = [
    'Alpha Allen',
    'Bravo Brittany',
    'Charlie Charlie',
    'Delta Dave',
    'Echo Eddie',
    'Foxtrot Frank',
    'Golf Greg',
    'Hotel Henry',
    'India Izzie',
    'Juliett James'
]

# Lists of Attacks
attacks = ['Fire', 'Earth', 'Water']

# ---------------------------------

player = randomator(characters)
opponent = randomator(characters)

while player == opponent:
    opponent = randomator(characters)

print (player + ' vs ' + opponent)

pscore = 0
oscore = 0
gameover= False

while gameover == False:

    # Game Toggle
    if pscore >= 3 or oscore >= 3:
        print ('Game Over!')
        print ('Final Score: ' + player + ': ' + str(pscore) + ' - ' + opponent + ': ' + str(oscore))
        gameover = True
        break

    # Game Score Update
    print ('Score: ' + player + ': ' + str(pscore) + ' - ' + opponent + ': ' + str(oscore))

    # Pick Attacks
    while True:
        try:
            pattack = int(raw_input("Enter [1] Fire, [2] Earth or [3] Water: "))
            break
        except ValueError:
            print ('Please select 1, 2, or 3 ONLY')

    # User Attack Converter
    if pattack == 1:
        pattack = 'Fire'
    elif pattack == 2:
        pattack = 'Earth'
    elif pattack == 3:
        pattack = 'Water'
    elif pattack >= 4:
        print ("You have chosen an invalid attack. A random attack has been chosen for you.")
        pattack = randomator(attacks)

    oattack = randomator(attacks)

    while pattack == oattack:
        oattack = randomator(attacks)

    print (" ")

    # --------------------------------

    # Displaying Attacks Chosen
    print (player + ' attacks with ' + pattack)
    print (opponent + ' attacks with ' + oattack)

    # --------------------------------

    # Battle Conditional: Fire > Earth > Water
    if pattack == "Fire" and oattack == "Earth":
        print (player + " defeats " + opponent)
        pscore += 1
    elif pattack == 'Earth' and oattack == 'Water':
        print (player + 'defeats' + opponent)
        pscore += 1
    elif pattack == 'Water' and oattack == 'Fire':
        print (player + " defeats " + opponent)
        pscore = + 1
    elif oattack == 'Fire' and pattack == 'Earth':
        print (opponent + ' defeats ' + player)
        oscore += 1
    elif oattack == 'Earth' and pattack == 'Water':
        print (opponent + ' defeats ' + player)
        oscore += 1
    elif oattack == 'Water' and pattack == 'Fire':
        print (opponent + ' defeats ' + player)
        oscore += 1