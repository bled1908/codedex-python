# # Instance Methods
# Now that we can create classes and objects, and edit their properties, our last step is to create functions.

# Wait... functions in classes?! Isn't that super complicated?

# Actually, it's not. Functions that are defined in a class are called methods. In fact, we have already used a bunch of methods. For example, in exercise 25, we looked at a few built-in list methods, such as:

# .insert()
# .append()
# .remove()
# These are built-in methods. Let's create our own methods within a class!

# Consider our Student class:

# class Student: 
#   def __init__(self, name, year, enrolled, gpa):
#     self.name = name
#     self.year = year
#     self.enrolled = enrolled
#     self.gpa = gpa

# To implement a method, we need to define one inside the class. For example, if we want to create a method called .display_info(), we would define it like so:

# class Student: 
#   def __init__(self, name, year, enrolled, gpa):
#     self.name = name
#     self.year = year
#     self.enrolled = enrolled
#     self.gpa = gpa
  
#   def display_info(self):
#     print('The student ' + self.name + '\'s GPA is ' + str(self.gpa) + '!')

# But remember, like a function, defining a method doesn't automatically run the code inside the method's body. We still need to call the method as follows:

# mitsuha = Student('宮水三葉', 11, False, 4.0)
# taki = Student('立花瀧', 11, True, 3.8)

# mitsuha.display_info()
# taki.display_info()

# # Output:
# # The student 宮水三葉's GPA is 4.0!
# # The student 立花瀧's GPA is 3.8!

# Note: Take a look at def display_info(self). Like what we learned about with the __init__() method, the first argument in the methods we make is always self. Every method has to have this self argument. The object attached to the method call is what self refers to.

# In our example, we created two objects, mitsuha and taki.

# When we called the mitsuha.display_info() method, the self parameter refers to the mitsuha object.
# In the case of taki.display_info(), self refers to the taki object.
# Also, you can define as many methods as you'd like!

# class Student: 
#   def __init__(self, name, year, enrolled, gpa):
#     self.name = name
#     self.year = year
#     self.enrolled = enrolled
#     self.gpa = gpa
  
#   def display_info(self):
#     print('The student ' + self.name + '\'s is ' + str(self.gpa) + '!')
  
#   def graduation(self):
#     if self.enrolled and self.gpa > 2.5 and self.year == 12:
#       print(self.name + ' will be able to graduate this year!')

# Write code below 💖

class BankAccount:
  def __init__(self, first_name, last_name, account_id, account_type, pin, balance):
    self.first_name = first_name
    self.last_name = last_name
    self.account_id = account_id
    self.account_type = account_type
    self.pin = pin
    self.balance = balance

  def deposit(self, money):
    self.balance += money
    return self.balance

  def withdraw(self, money):
    self.balance -= money
    return money
  
  def display_balance(self):
    print(f"Balance: {self.balance}")
  
subha_account = BankAccount("Subhadeep", "Roy", 1001, "Savings", 1002, 1000000000)
print(subha_account.deposit(1000000))
print(subha_account.withdraw(1000))
subha_account.display_balance()