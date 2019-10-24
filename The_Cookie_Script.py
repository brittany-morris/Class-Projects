# Brittany Morris
# Python 2.7 (SSF1910)
# The Cookies Script


### The Cookie Script ###

name = raw_input("Enter Name: ")
appetite = "hungry"
cookies = True
cookie_count = 10

while cookies == True:
    if appetite == "hungry" and cookie_count >0:
        print(name + " is " + appetite)
        print(name + ' ate a cookie ')
        cookie_count -= 1
        print("There are " + str(cookie_count) + " left.")
    else:
        appetite = "not hungry"
        cookies = False
        print(name + " is " + appetite)
        print(name + " is full of cookies!")