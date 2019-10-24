# Brittany Morris
# Python 2.7 (SSF1910)
# Activity: Conditional Statements and Control Flow

### Part 1: Congressional Conditional ###

age = input("Enter Age: ")
citizenship = input("Enter Number of Years as a US Citizen: ")

if age >= 30 and citizenship >= 9:
    result = "You are eligible for the Senate and the House"
elif age >= 25 and citizenship >= 7:
    result = "You are eligible for the House of Representatives."
else:
    result = "You are ineligible to serve."

print result

