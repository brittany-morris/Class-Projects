# Brittany Morris
# Python 2.7 (SSF1910)
# Activity: Exception Handling

import random
import time

# Custom Functions
# 2. Define a custom function called agecheck() that will allow the user
# to enter their age as a NUMBER

agecheck = int(raw_input('Enter Age: '))


# 3. Describe how the countdown() function works
''' The countdown function works by allowing the user to select the starting amount of seconds. Each 
second that is counted is delayed and once the second is counted a second is subtracted from 
the number before.'''
# You may replace this function with one you created
def countdown(n):
    while n >= 0:
        print n
        time.sleep(1)
        n -= 1

# 4. List the Local & Global variables used throughout this script
''' Global: print --- Local: rank '''
# 5. List the Built-In functions used throughout this script
'''countdown, self_destruct'''
# 6. List the Module functions used throughout this script
'''try '''
# 7. List the Custom functions used throughout this script
'''rank, initiate, authorized_test, authorized_final'''

# Self Destruct Sequencer
# This is the custom function created to handle all of the Self Destruct
# features needed. There are a few steps involved in the process, so take a few
# moments to study how this function works and think about ways to make it better.
def self_destruct(x):

    # Set Destruct Codes
    authorized_test = "000-Destruct-0"
    authorized_final = "000-Destruct-1"

    # 8. Create variables (similar to above) for the Commanding Officer's CODE (co_code),
    # Executive Officer's CODE (xo_code) & Chief Engineer's CODE (ce_code)

    co_code = "comoff1"
    xo_code = "exoff2"
    ce_code = "chief3"

    # Consider the following print statements. Could they be combined into a single print
    # statement and get the same result? (Answer: Yes) There are many ways to resolve
    # issues in scripting. You get to decide what works best for your script.
    #  Display Self Destruct Warning
    print "--------------------- WARNING! ----------------------"
    print "You have initiated the USR ARES Self Destruct Program"
    print "_____________________________________________________"
    print "You must provide Authorized Initiate Code to Proceed."

    # This next section of code is designed to prevent the user from
    while True:
        try:
            # Request Authorized Rank
            # 9. Explain the significance of the int() below:
            '''int requires the input to be a number.'''
            rank = int(raw_input(
                "Select Correct Rank:\n [1] Commanding Officer\n [2] Executive Officer\n [3] Chief Engineer\n RANK: "))

            # Because we're expecting the user to enter a number above, the conditional statement
            # below is needed to convert those numbers into something more useful. Doing this helps
            # reduce the risk of the user introducing bad data into the script.

            # Retrieve Rank Initiate Code
            # 10. Replace the string values for the code with the corresponding variable from
            # step 8.
            # Commanding Officer
            if rank == 1:
                code = "comoff1"
                print "Commanding Officer Confirmed."
                break
            
            # Executive Officer
            elif rank == 2:
                code = "exoff2"
                print "Executive Officer Confirmed."
                break
            # Chief Engineer
            elif rank == 3:
                code = "chief3"
                print "Chief Engineer Confirmed."
                break
            else:
                print "You are not authorized to initial Self Destruct."
        except:
            print "You have entered an invalid code. Please try again."

    # Set Supplied Rank Code
    initiate = raw_input("Enter Self Destruct Confirmation Code: ")

    # Compare Rank Codes
    if initiate == code:
        print "Self Destruct Initiate Code: ACCEPTED"
        final_code = raw_input("Enter Activation Code: ")

        # In Part 2, you wil need to add exception / error handling to this part of the script.
        if final_code == authorized_final:
            print "Destruct Sequence Confirmed."
            # 10. EXPLAIN THE SIGNIFICANCE OF THE str() FUNCTION HERE
            print str(x) + " seconds to Self Destruct."
            print "ALL HANDS ABANDON SHIP - THIS IS NOT A DRILL"
            countdown(x)
            print "Have a nice day!"
            print "BOOM!"
        elif final_code == authorized_test:
            print "Destruct Sequence Test Order Confirmed."
            print "THIS IS A DRILL - THIS IS A DRILL"
            print "Timer Set to: " + str(x) + " seconds."
        else:
            print "Destruct Sequence Aborted."



# Self Destruct

timer = int(raw_input("Enter Countdown Length (in seconds): "))

self_destruct(timer)