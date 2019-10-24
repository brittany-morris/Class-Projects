# Brittany Morris
# Python 2.7 (SSF1910)
# Activity: Dictionary Searches

'''
We start with an empty states bracket because we do not want to define what is being
place in there. We want to import the text list with the code following.
'''

states = {}

'''
The for loop is used to run through the list of the states and their capitals
by separating them by the comma.
'''

with open ('states.txt', 'r') as f:
    for line in f:
        (key,val) = line.split(',')
        states[key] = val

print ('STATE SEARCH SCRIPT')
print ('Please enter the name of 5 states to search for.')

count = 5

f = open('state_results.txt', 'w+')

# 5.
# By defineing count as 5 that will cause our for loop to make the user enter a state 5 times.
# It creates a limit that needs to be reached before the completion of the code.

# 6.
# The count variable can be updated by redefining count.

# 7.
# The number of states needed to be entered will be changed going forward in the script

# 8.
# states[search] will check the text file for the corresponding key: value

for x in range(count):
    search = str(raw_input('Enter Name of City: ')).title()

    if search in states:
        print ('The Capital of ' + search.title() + " is " + str(states[search]))
        count -=1
        print ('Remaining number of searches: ' + str(count))
        f.write('State: ' + search + ' Capitol: ' + states[search])
    else:
        print ("You've entered an invalid value.")
f.close()



