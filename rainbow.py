# Brittany Morris
# Python 2.7.10
# Activity: Correcting Scripts


colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']

# print "The colors in the Rainbow are: '
print "The colors in the Rainbow are: "

'''
for color in colors
    print color 
'''
for color in colors:
    print color



'''
  File "/Users/brittanymorris/Desktop/Cloud Technologies/System Scripting Fundamentals/Module 1/SSF1910/rainbow.py", line 8
    print "The colors in the Rainbow are: '
                                          ^
SyntaxError: EOL while scanning string literal

Why the error occured: The first error is that the first print statement mixes the type of quotes. 
It starts the statement with double quotes and ends it with single quotes. 
'''

'''
 File "/Users/brittanymorris/Desktop/Cloud Technologies/System Scripting Fundamentals/Module 1/SSF1910/rainbow.py", line 11
    for color in colors
                      ^
SyntaxError: invalid syntax

Why the error occured: The reason for the error is that the for statement was missing the : at the end. 
'''

