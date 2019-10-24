# Brittany Morris
# Python 2.7 (SSF1910)
# Notes: Nesting Loops and Complex Loops

# Nesting Loops

for x in xrange(1,4):
    for y in xrange (0,6,2):
        print "Outer Loop (x): " + str(x) + " Inner Loop (y): " + str(y)



# Complex Loop Structures
cookies = 10

hungry = True

while hungry == True:
    if cookies >= 1:
        print "You have eaten a cookie."
        #cookies = cookies - 1
        cookies -= 1
        print "There are " + str(cookies) + " cookies left."
    else:
        print "You have eaten all the cookies."
        hungry == False
        break



# Loop Summary
### See the Cookie Script
