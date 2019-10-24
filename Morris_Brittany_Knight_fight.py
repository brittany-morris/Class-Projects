# Brittany Morris
# Python 2.7.10
# Tale of the Black Knight

# The random module provides access to random related functions
# The time module provides access to time related functions
import random
import time

goodguy = str(raw_input("Enter your Knight's Name: "))
goodguy = "Sir " + goodguy

# Here, we are assigning the value 'The Black Knight' to the variable badguy
# 1. CHANGE THIS LINE SO THE USER CAN ENTER A VALUE FOR BADGUY
badguy = str(raw_input("Enter the Bad Guy's Name: "))
badguy = "Sir " + badguy

# Once Upon A Time...
print goodguy + ", a Knight in search of adventure, is wandering through the enchanted forest one day."

# 2. WHAT ACTION IS THIS LINE PERFORMING?
# time.sleep creates a delay so that the text does not show up all at once.
time.sleep(2)

print "As " + goodguy + " reaches a clearing, he encounters the fearsome " + badguy + "!"

time.sleep(2)

print goodguy + ": You, Sir, are a Blackguard and a coward! I challenge you to a duel!"
print badguy + ": I'mma cut you, fool!"

# Sir Dudus Health
gghealth = 100
# Black Knight Health
bghealth = 100

# Fight Sequence Loop
while gghealth > 0:
    # 3. EXPLAIN HOW GOODGUY / BADGUY HIT POINTS ARE GENERATED
    # Good guy and bad guy hit points are generated randomly picking a number between 1 and 99
    # Good Guy / Bad Guy Hit Points
    gghit = random.randint(1,100)
    bghit = random.randint(1, 100)
    # #######################################################

    # 4. WHAT PURPOSE DOES '\n' SERVE?
    # '\n' created a new line in the script.
    print "\n"

    # 5. FIND & CORRECT THE SYNTAX ERRORS. COMMENT OUT THE INCORRECT LINE AND
    # WRITE THE CORRECT CODE UNDERNEATH
    '''print goodguy + " rolls a " + gghit
    print badguy + " rolls a " + bghit'''

    print goodguy + " rolls a " + str(gghit)
    print badguy + " rolls a " + str(bghit)

    # 6. EXPLAIN HOW THE VALUE IN DAMAGE IS CALCULATED
    # The good guy hit points are subtracted by the bad guy hit points
    # Damage Calculator
    if gghit > bghit:

        damage = gghit - bghit
        bghealth = bghealth - damage
        print goodguy + " strikes " + badguy + " for a " + str(damage) + " hit!\n"

        if bghealth >= 0:
            print badguy + ": I am beaten. Well fought...\n"
            break
        elif bghealth >= 25:
            print badguy + ": Thou art a worthy opponent.\n"
        elif bghealth >= 50:
            print badguy + ": Alas! A fair strike! En garde!\n"
        elif bghealth >= 75:
            print badguy + ": Tis but a flesh wound.\n"
        elif bghealth >= 0:
            print badguy + ": Thou hast missed.\n"
    # #######################################################
    elif bghit > gghit:

        damage = bghit - gghit
        gghealth = gghealth - damage

        # 7. EXPLAIN WHY THE str() FUNCTION IS NEEDED HERE
        # The str() is needed so that you can combine a string and an integar together.
        print badguy + " strikes " + goodguy + " for a " + str(damage) + " hit!\n"

    # 8. CORRECT THE FLAW IN THE CONDITIONAL STATEMENT BELOW (HINT: It's not a syntax error)
        '''if gghealth >= 0:
            print goodguy + ": Thou hast missed.\n"
            break
        elif gghealth >= 25:
            print goodguy + ": Tis but a flesh wound.\n"
        elif gghealth >= 50:
            print goodguy + ": Alas! A fair strike! En garde!\n"
        elif gghealth >= 75:
            print goodguy + ": Thou art a worthy opponent.\n"
        elif gghealth <= 0:
            print goodguy + ": I am beaten. Well fought.\n"
            '''

        if gghealth >= 0:
            print badguy + ": I am beaten. Well fought...\n"
            break
        elif gghealth >= 25:
            print badguy + ": Thou art a worthy opponent.\n"
        elif gghealth >= 50:
            print badguy + ": Alas! A fair strike! En garde!\n"
        elif gghealth >= 75:
            print badguy + ": Tis but a flesh wound.\n"
        elif gghealth >= 0:
            print badguy + ": Thou hast missed.\n"

    # #######################################################

# END OF LOOP ###############################################

# 9. PRINT A CONGRATULATORY STATEMENT HERE USING THE NAME OF THE WINNER (GOODGUY OR BADGUY)
print "End of the Knight Fight\n"

if gghealth > 0:
    print "Congratulations " + goodguy + "!"
else:
    print "Congratulations " + badguy  + "!"

# 10. AFTER completing Part 2 below, upload your completed script as a .zip file to FSO

# PART 2
'''
In your own words, answer the following 4 questions on the use of the WHILE Loop in the script from Part 1:

    1. What Condition will end the WHILE Loop?
    # break
    2. How is that Condition handled in the code?
    # It will stop the sequence after the desired outcome is reached
    3. What events happen inside the WHILE Loop?
    # It runs continously until a condition is met. 
    4. Why are gghealth & bghealth initially set outside the WHILE Loop?
    So that they stop running when it is appropiate. 
'''