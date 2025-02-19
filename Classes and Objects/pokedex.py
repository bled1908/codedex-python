# We learned how to:

# Create a class and initialize them with certain attributes.
# Create objects based on these classes and set values for these attributes.
# Create classes using the special __init__() method.
# Create instance methods that will update or use these class attributes.

# Write code below 💖

class Pokemon:
  def __init__(self, entry, name, types, description, is_caught, level, region, height, weight):
    self.entry = entry
    self.name = name
    self.types = types
    self.description = description
    self.is_caught = is_caught
    self.level = level
    self.region = region
    self.height = height
    self.weight = weight
  
  def speak(self):
    print(self.name + " " + self.name)
  
  def display_details(self):
    print(f'''Entry Number: {self.entry}
Name: {self.name}
Type: {self.types}
Description: {self.description}''')
    if self.is_caught:
      print(self.name + " has already been caught!")
    else:
      print(self.name + " has not been caught!")
    print(f'''Level: {self.level}
Region: {self.region}
Height: {self.height}
Weight: {self.weight}\n''')

bulbasaur = Pokemon(1, "Bulbasaur", ["Grass", "Poison"], "For some time after its birth, it uses the nutrients that are packed into the seed on its back in order to grow.", True, 1, "Kanto", "2' 04\"", "15.2 lbs")
bulbasaur.speak()
bulbasaur.display_details()

charmander = Pokemon(4, "Charmander", ["Fire"], "The flame on its tail shows the strength of its life-force. If Charmander is weak, the flame also burns weakly.", True, 1, "Kanto", "2' 00\"", "18.7 lbs")
charmander.speak()
charmander.display_details()

squirtle = Pokemon(7, "Squirtle", ["Water"], "After birth, its back swells and hardens into a shell. It sprays a potent foam from its mouth.", False, 1, "Kanto", "1' 08\"", "19.8 lbs")
squirtle.speak()
squirtle.display_details()