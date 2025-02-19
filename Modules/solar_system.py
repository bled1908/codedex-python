# # The from Keyword
# What if we wanted to import a piece of a module instead of the whole thing? We can use the from keyword!

# At the top of our file, this keyword goes before the import keyword:

# from module_name import objects

# We can use the from keyword to import one or more objects from a module, such as built-in classes, methods, or variables.

# The next example uses the from keyword to import random module's .sample() method that returns a list of values randomly picked from another list:

# from random import sample

# famous_houses = [
#   '🐺 Stark',
#   '🐉 Targaryen',
#   '🦌 Baratheon',
#   '🦑 Greyjoy',
#   '🦁 Lannister'
# ]

# example = sample(famous_houses, 2)

# print(f'Example: {example}')

# Since the .sample() method was directly imported, we can just write sample() instead of the usual random.sample().

# By the way, more than one method, variable, or class can be imported from a module on a single line.

# If we want to import both the .choice() and .sample() methods:

# from random import choice, sample

# Note: The random.choice() method randomly selects and returns a single element from a list.

# # The as Keyword
# Some module names are long, and it can be unpleasant to write the word repeatedly. This is where aliasing can be helpful!

# We can nickname a module by using the as keyword. This is called aliasing.

# For example:

# import random as rd

# Here, we are renaming the random module with a shorthand, rd.

# From this point of the program, the random module will be known as rd.

# The from and as keywords can also be combined:

# from random import sample as samp

# example = samp(['Stark', 'Targaryen', 'Baratheon', 'Greyjoy', 'Lannister'], 2)

# print('Example: ' + example[0] + ' ' + example[1])

# Instead of typing sample(), we can use the alias we assigned it to, samp().

# Write code below 💖
from math import pi
from random import choice as ch

planets = [
  'Mercury',
  'Venus',
  'Earth',
  'Mars',
  'Saturn'
]

random_planet = ch(planets)

if random_planet == "Mercury":
  r = 2440
elif random_planet == "Venus":
  r = 6052
elif random_planet == "Earth":
  r = 6371
elif random_planet == "Mars":
  r = 3390
elif random_planet == "Saturn":
  r = 58232
else:
  print("Oops! An error occurred.")

area = round(4 * pi * r**2)

print(f"Area of {random_planet}: {area} sq mi.")