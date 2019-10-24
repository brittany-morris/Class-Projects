# Brittany Morris
# Python 2.7 (SSF1910)
# Notes: Working with Dictionaries

# Searching for Values in a dictionary

teams = {
    'Arizona': 'Diamondbacks',
    'New York': ['Dodgers', 'Giants', 'Mets', 'Yankees'],
    'Washington': ['Nationals', 'Senators']
}

# Loop 5 times
# Add some error / exception handling

print ("Welcome to MLB Search")
print ("You must enter the name of a City / State to see the MLB teams that play there or have played there.")

search = str(raw_input('Enter Name of City: ')).title()

if search in teams:
    print ('Franchise(s) that played in ' + search.title() + ": " + str(teams[search]))
else:
    print ("You've entered an invalid term.")


# Importing Data into a Dictionary

states = {}

with open('states.txt', 'r') as f:
    for line in f:
        (key,val) = line.split(',')
        states[key] = val

print states['Arizona']
