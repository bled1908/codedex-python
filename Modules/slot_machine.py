# 39. Slot Machine
# # Modules
# Welcome to the final chapter of The Legend of Python! 🐍

# Here, we are going to take a deep dive into something called modules.

# A module is any file with a .py extension. But more ideally, a module contains statements, functions, and class definitions that revolve around a similar purpose.

# By default, Python comes with over 200 modules that we can use.

# Here are some examples:

# random module to generate a random number.
# math module to calculate the square root.
# datetime module to work with dates and times.
# Modules are magical because they offer us tools and method to solve a problem that we'd otherwise have to write ourselves.

# In this chapter, we will use built-in modules first before creating our own.

# # Random Choices
# Let's revisit a module we've already worked with before: the random module!

# Remember when we used the .randint() method to generate a random number in the Magic 8 Ball? Well, there are 22 methods total in the random module.

# Here's another method, .choices(), in action:

# import random

# dice = [1, 2, 3, 4, 5, 6]

# print(random.choices(dice))

# The import keyword is used to access the random module.
# The .choices() method will randomly select a single item by default.
# We can also set how many items are randomly chosen with the k parameter:

# import random

# dice = [1, 2, 3, 4, 5, 6]

# print(random.choices(dice, k=3))

# This will return a new list of three items randomly selected from dice. Every time you run it, the output should be different.

# Note: The k parameter only sets the length of the returned list from .choices(). This means that a list item may be included in the returned list more than once.

# # Multiple Modules
# There are two ways to import two or more modules at the top of our program:

# With multiple import statements:
# import random
# import math

# # Rest of the code...

# With one import statement and modules separated by commas:
# import random, math

# # Rest of the code...

# These two code blocks do the exact same thing.

# Write code below 💖
import random

def play():
  to_play = True
  symbols = ['🍒',' 🍇', '🍉', '7️⃣']
  while to_play:
    a = random.choice(symbols)
    b = random.choice(symbols)
    c = random.choice(symbols)
    print(a + " | " + b + " | " + c)
    if a == b == c == '7️⃣':
      print("Jackpot! 💰")
    else:
      print("Thanks for playing!")
    choice = input("Want to play again? (Y/N): ").upper()
    if choice != "Y":
      to_play = False
    print("\n")

play()

# # Slot Machine 🎰
# # Codédex

# import random

# symbols = [
#   '🍒',
#   '🍇',
#   '🍉',
#   '7️⃣'
# ]

# def play():

#   for i in range(1, 51):    
#     results = random.choices(symbols, k=3)
#     print(f'{results[0]} | {results[1]} | {results[2]}')
#     win = results[0] == '7️⃣' and results[1] == '7️⃣' and results[2] == '7️⃣'

#     if win:
#       print('Jackpot!!! 💰')
#       break
#     else:
#       results = random.choices(symbols, k=3)

# answer = ''
# while answer.upper() != 'N':
#   play()
#   answer = input('Keep playing? (Y/N) ')

# print('Thanks for playing!')