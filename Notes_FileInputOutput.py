# Part 1: Importing Text Files into a List

# Ways to open a text file in Python

## Permissions
# W is write,
# W+ is python can make a blank document with that name if file doesn't exist
# r is read only,
# a is append

### Basic Input ###
### Open an existing file
# f = open (filename.txt, 'permission letter')
# list = f.read().splitlines()
# f.close()


# Part 2: Using with open() and exporting data to a text file

movies = [
    'Bull Durham',
    'Field of Dreams',
    'The Natural',
    'A League of Their Own',
    'The Sandlot',
    'The Bad News Bears',
    'Major League',
    'Rookie of the Year',
    '42',
]

with open('baseball_movies.txt', 'w+') as f: