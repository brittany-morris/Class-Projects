# Brittany Morris
# Python 2.7 (SSF1910)
# Activity: Grade Conversion

score = int(raw_input("Enter assignment score: "))

if score >= 95:
    grade = "A+"
elif score >= 90:
    grade = "A"
elif score >= 85:
    grade = "B+"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"


print "You earned a " + grade + " for this assignment."

