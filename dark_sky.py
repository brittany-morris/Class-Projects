# Brittany Morris
# Python 2.7
# Dark Sky API

# Dark Sky Weather
# sudo pip install --update
# sudo pip install future

from darksky import forecast

# You need to create an account to get your API Key
API_KEY = 'fa06dbd47920af62d009893032af73db'

# Use your Hometown, where you currently live and 5 places you want to visit
# before the Sweet Meteor of Doom wipes out humanity.

# Hometown
PITTSBURGH = darksky.forecast(API_KEY, 40.4406, 79.9959)

# Current
PHOENIX = darksky.forecast(API_KEY, 33.4484, 112.0740)

# 5 places to visit
DUBLIN = darksky.forecast(API_KEY, 53.4129, 8.2439)
MOSCOW = darksky.forecast(API_KEY, 55.7558, 37.6173)
SALEM = darksky.forecast(API_KEY, 42.5215, 70.8989)
BOSTON = darksky.forecast(API_KEY, 42.3601, 71.0589)
SEATTLE = darksky.forecast(API_KEY, 47.6062, 122.3321)

print ("Phoenix Daily Summary: \n" + PHOENIX.daily.summary + '\n' )
print ("Pittsburgh Current Temperature: " + str(PITTSBURGH.currently.temperature))
print ("Pittsburgh Current Temperature: " + str(int(PITTSBURGH.currently.temperature)) + '\n')

print ("Dublin Daily Summary: \n" + DUBLIN.daily.summary + '\n')
print ("MOSCOW Daily Summary: \n" + MOSCOW.daily.summary + '\n')
print ("SALEM Daily Summary: \n" + SALEM.daily.summary + '\n')
print ("BOSTON Daily Summary: \n" + BOSTON.daily.summary + '\n')
print ("SEATTLE Daily Summary: \n" + SEATTLE.daily.summary + '\n')
