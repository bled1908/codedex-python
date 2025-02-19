# Challenge 1 - James Bond

# Write code below 💖

def greetings(first_name, last_name):
  print(f"{last_name}, {first_name} {last_name}")

greetings("Subhadeep", "Roy")

# Challenge 2 - Average Number

# Write code below 💖

average = lambda num1, num2: (num1 + num2)/2

print(average(2, 4))

# Challenge 3 - KDA Ratio

# Write code below 💖

kda = lambda k, d, a: (k + a)/ d

print(kda(5, 1, 4))

# Challenge 4 - Moon Phases

# Write code below 💖

def moon_phase(phase):
  if phase == "New Moon":
    return "🌑"
  elif phase == "Waxing Crescent":
    return "🌒"
  elif phase == "First Quarter":
    return "🌓"
  elif phase == "Waxing Gibbous":
    return "🌔"
  elif phase == "Full Moon":
    return "🌕"
  elif phase == "Waning Gibbous":
    return "🌖"
  elif phase == "Last Quarter":
    return "🌗"
  elif phase == "Waning Crescent":
    return "🌘"
  else:
    return "Invalid moon phase"

answer = moon_phase('New Moon')
print(answer)

# Challenge 5 - Dog Years

# Write code below 💖

def dog_years(name, age):
  return f"{name} is {age * 7} years old in human years."

print(dog_years('Landon', 3))
print(dog_years('Red Bean', 6))
print(dog_years('Cooper', 2))