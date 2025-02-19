# # Objects
# Now that we know how to create a class, we can create objects from this class.

# An object is an "instance" of a class. A class is simply a template to create objects, which are individual copies of the class with actual values.

# In the last exercise, we created a class to model students:

# class Student:
#   student_id = 0
#   name = ''
#   year = 0
#   gpa = 0.0
#   enrolled = False

# Using the Student class, let's create an object to model the infamous student, Ferris Bueller. The syntax for creating an object looks like this:

# ferris = Student()

# Now that we have created an object of Student and saved it to ferris, we can access and edit the class attributes by using the dot syntax, .attribute:

# ferris.student_id = 10837
# ferris.name = 'Ferris Bueller'
# ferris.year = 12
# ferris.gpa = 3.81
# ferris.enrolled = True

# Ferris Bueller is a 12th year student with a GPA of 3.81 and is currently enrolled. So we now know how to get him out of a class! 💨

# You can check all the attributes available on the ferris object with the built-in vars() function, as follows:

# print(vars(ferris))

# # Output: {'student_id': 10837, 'name': 'Ferris Bueller', 'year': 12, 'gpa': 3.81, 'enrolled': True}

# We don't have to stop there; we can create as many students as we want using just one Student class.

# Write code below 💖

class Restaurant:
  name = ''
  category = ''
  rating = 0.0
  delivery = False

bobs_burgers = Restaurant()
bobs_burgers.name = 'Bob\'s Burgers'
bobs_burgers.category = 'American Diner'
bobs_burgers.rating = 4.7
bobs_burgers.delivery = False

kfc = Restaurant()
kfc.name = "Kentucky Fried Chicken"
kfc.category = "Fast Food"
kfc.rating = 4.5
kfc.delivery = True

dominos = Restaurant()
dominos.name = "Domino's Pizza"
dominos.category = "Fast Food"
dominos.rating = 4.0
dominos.delivery = True

print(vars(bobs_burgers))
print(vars(kfc))
print(vars(dominos))