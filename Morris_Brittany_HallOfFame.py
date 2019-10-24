# Brittany Morris
# Python 2.7 (SSF1910)
# Activity: Hall of Fame Players

favorite_baseball_player = "Old Hoss Radbourne"

with open("hall_of_fame.txt", 'w+') as f:
    f.write("Bobby Bonds\n")
    f.write("Al Kaline\n")
    f.write("Mickey Mantle\n")
    f.write("Willie Mays\n")

    # 5. Using the f.write() function, add the player stored in
    # favorite_baseball_player to the hall_of_fame.txt file
    # Note: You MUST reference the variable in this part.

    f.write(favorite_baseball_player)
    f.write('\n')

# 6. Replace the r with the appropriate option for appending the file.
# with open('hall_of_fame.txt', 'r') as f:
# 7. Using the f.write() function, add 3 more players the list:
# [Babe Ruth, Willie Stargell & Roberto Clemente]

with open('hall_of_fame.txt', 'a') as f:
    f.write('Babe Ruth\n')
    f.write('Willie Stargell\n')
    f.write('Roberto Clemente\n')


# 8. Using with open(), place the values stored in hall_of_fame.txt into a variable called hof_players

f = open('hall_of_fame.txt', 'r')
hof_player = f.read().splitlines()
f.close()


# 9. Write a print statement below with the MLB Team closest to your Home Town.
# print mlb[18]

f = open('mlb_teams.txt', 'r')
mlb = f.read().splitlines()
f.close()
print (mlb[0])


# 10. Write a print statement to print one of the players stored in the variable hof_players created in step 8.

print (hof_player[2])