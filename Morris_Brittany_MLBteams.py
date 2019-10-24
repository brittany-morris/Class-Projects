# Brittany Morris
# Python 2.7 (SSF1910)
# Activity: MLB Teams


# w write permissions
# w+ write permissions w\create blank doc
# r read only permission
# a append

#######################
# MLB TEAMS
#######################

# 2. The example below uses the old method of opening an external file.
# Convert the open() function below [line 16 - 18 ]to with open().

# Baseball Team Text file import
'''
f = open('mlb-teams.txt', 'r')
mlb = f.read().splitlines()
f.close()
'''

f = open('mlb_teams.txt', 'r')


# 3. Replace the w+ with the appropriate option for appending the file.
### with open('mlb-teams.txt', 'w+') as f:

f = open('mlb_teams.txt', 'a')
f.write('Seattle Pilots\n')
f.write('Washington Senators\n')
f.write('Montreal Expos\n')

    # 4.  Using the f.write() function, add three more teams to the list:
    # [ Seattle Pilots, Washington Senators & Montreal Expos ]