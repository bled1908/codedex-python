# Challenge 1 Food Ratings

# Write code below 💖

rating = 5.0

if rating > 4.5:
  print("Extraordinary")
elif rating > 4:
  print("Excellent")
elif rating > 3:
  print("Good")
elif rating > 2:
  print("Fair")
else:
  print("Poor")
  
# Challenge 2 High Shool Grades

# Write code below 💖

grade = int(input("Enter your grade: "))

if grade == 9:
  print("Freshman")
elif grade == 10:
  print("Sophomore")
elif grade == 11:
  print("Junior")
elif grade == 12:
  print("Senior")
else:
  print("TBD")
  
# Challenge 3 Snapple facts

# Write code below 💖
import random

num = random.randint(0, 5)

if num == 0:
  print("Flamingos turn pink from eating shrimp.")
elif num == 1:
  print("The only food that doesn\'t spoil is honey.")
elif num == 2:
  print("Shrimp can only swim backwards.")
elif num == 3:
  print("A taste bud\'s life span is about 10 days.")
elif num == 4:
  print("It is impossible to sneeze while sleeping.")
elif num == 5:
  print("It is illegal to sing off-key in North Carolina.")
  
# Challenge 4 Seasons of the year

# Write code below 💖

month = int(input("Enter Month Number: "))

if month == 1 or month == 2 or month == 3:
  print("Winter 🌨️")
elif month == 4 or month == 5 or month == 6:
  print("Spring 🌱")
elif month == 7 or month == 8 or month == 9:
  print("Summer 🌻")
elif month == 10 or month == 11 or month == 12:
  print("Autumn 🍂")
else:
  print("Invalid")
  
# Challenge 5 Planet Weights

# Write code below 💖

earth_weight = float(input("Enter your weight in earth in kg: "))
planet_number = int(input("Enter planet number: "))
destination_weight = 0

if planet_number == 1:
  destination_weight = earth_weight * 0.38
elif planet_number == 2:
  destination_weight = earth_weight * 0.91
elif planet_number == 3:
  destination_weight = earth_weight * 0.38
elif planet_number == 4:
  destination_weight = earth_weight * 2.53
elif planet_number == 5:
  destination_weight = earth_weight * 1.07
elif planet_number == 6:
  destination_weight = earth_weight * 0.89
elif planet_number == 7:
  destination_weight = earth_weight * 1.14
else:
  print("Invalid planet number")

print(f"Your destination weight is {destination_weight}")