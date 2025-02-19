# Write code below 💖

height = int(input("Enter height(in cm): "))
credits = int(input("Enter Credits: "))

if height > 137 and credits > 10:
  print("Enjoy the ride!")
elif not(height > 137) and credits > 10:
  print("You are not tall enough to ride.")
elif height > 137 and not(credits > 10):
  print("You don't have enough credits.")
else:
  print("You are neither tall enough nor have enough credits.")