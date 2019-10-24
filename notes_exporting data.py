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

    for film in movies:
        print (film + " Starring: ")
        star = raw_input("Enter Actor Name: ")
        f.write(film + " - " + star)
        f.write("\n")