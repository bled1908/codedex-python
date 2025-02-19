# Challenge 1 Are we There Yet?

# Write code below 💖

answer = input("Are we there yet? ")

while answer != "Yes":
  answer = input("Are we there yet? ")
  
# Challenge 2 New Year Countdown

# Write code below 💖

for i in range(10, 0, -1):
  print(i)
print("Happy New Year! 🥳")

# Challenge 3 Dice Roll

# Write code below 💖
import random

dice1 = random.randint(1, 6)
dice2 = random.randint(1, 6)
dice_total = dice1 + dice2
total = 0

while total != dice_total:
  total = int(input("What is the total (2-12)? "))
print("You got it!")

# Challenge 4 Asterisks

# Write code below 💖

for i in range(1, 25):
  print("* " * i)
  
# Challenge 5 Sum of Squares

# Write code below 💖

number = int(input("Enter an integer: "))
total = 0

for i in range(1, number + 1):
  total += i ** 2
print(total)