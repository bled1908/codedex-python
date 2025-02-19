# # Create Your Own Module
# As discussed in a previous exercise, modules are essentially .py files that contain statements and definitions. So all of the files that were created for the exercises up to this point could be imported as a module!

# For example, recall the math functions defined in a previous exercise.

# If saved in a file called calculator.py, we could import it in a new file like so:

# import calculator

# Suppose we have another file called main.py, the functions from calculator.py (add(), subtract(), etc.) can be accessed and used with dot notation like so:

# import calculator
# import datetime

# calculator.add(3, 4)        # 7
# calculator.subtract(3, 4)   # -1
# calculator.multiply(3, 4)   # 12
# calculator.divide(3, 4)     # 0.75
# calculator.exp(3, 4)        # 27

# Note: The two files need to be in the same folder.

# # datetime Module
# Wait, what was that module? No, not calculator, the other one...

# The datetime module specializes in dates and times. Just like random, it comes with Python by default and can simply be imported.

# In addition to functions, modules may contain class object definitions with their own defined methods and properties.

# The datetime module has a date object that accepts the following properties:

# .year: An integer between 1 and 9999.
# .month: An integer between 1 and 12.
# .day: An integer between 1 and the number of days in a given month.
# The syntax for a date is datetime.date(year, month, day), like so:

# import datetime

# release_date = datetime.date(1991, 2, 20)
# print(release_date)     # Output: 1991-02-20

# The output shows the date object with a dash between each part. Also, any single number gets a leading zero 0.

# The .year, .month, and .day properties can be accessed like with any other class object:

# print(f'Python was released in {release_date.year}.')
# # Output: Python was released in 1991.

# Retrieving the current date is possible with the date.today() method:

# datetime.date.today()

import datetime, bday_messages

today = datetime.date.today()
next_birthday = datetime.date(2025, 8, 19)

days_away = next_birthday - today

if today == next_birthday:
  print(bday_messages.random_message)
else:
    print(f'My next birthday is {days_away.days} days away!')
   
# or    
# import datetime

# # Simulate the bday_messages module
# import random
# class bday_messages:
#     random_message = random.choice([
#         "Happy Birthday!",
#         "Wishing you a fantastic birthday!",
#         "Have an amazing birthday celebration!"
#     ])

# # Get today's date
# today = datetime.date.today()

# # Define your birth date (month and day only)
# birth_month = 8
# birth_day = 19

# # Calculate the next birthday dynamically
# current_year = today.year
# next_birthday = datetime.date(current_year, birth_month, birth_day)

# # If the next birthday is in the past, move to the next year
# if next_birthday < today:
#     next_birthday = datetime.date(current_year + 1, birth_month, birth_day)

# # Calculate the number of days until the next birthday
# days_away = (next_birthday - today).days

# # Output based on whether today is the birthday
# if today == next_birthday:
#     print(bday_messages.random_message)
# else:
#     print(f'My next birthday is {days_away} days away!')
