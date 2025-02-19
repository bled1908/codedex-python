# In this chapter, we learned:

# The "Don't Repeat Yourself" methodology.
# We've been using built-in functions like print() and input() all along.
# How to define and call a function — the two-step process.
# Inputs with parameters and arguments.
# Output with the return keyword.
# Function scope vs. global scope.

# Write code below 💖

def get_item(number):
  if number == 1:
    return '🍔 Cheeseburger'
  elif number == 2:
    return '🍟 Fries'
  elif number == 3:
    return '🥤 Soda'
  elif number == 4:
    return '🍦 Ice Cream'
  elif number == 5:
    return '🍪 Cookie'

def welcome():
  print('''Welcome to KFC!
  1. 🍔 Cheeseburger
  2. 🍟 Fries
  3. 🥤 Soda
  4. 🍦 Ice Cream
  5. 🍪 Cookie''')

def main():
  welcome()
  choice = int(input("What would you like? "))
  print(get_item(choice))

main()