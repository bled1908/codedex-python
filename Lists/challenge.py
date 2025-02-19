# Challenge 1 Wishlist

wishlist = ["Trendy Clothes", "skin care", "peace in life"]
print(wishlist)

# Challenge 2 Lottery

import random

my_numbers = []
winning_numbers = []

for _ in range(0, 5):
  my_numbers.append(random.randint(1, 69))
  winning_numbers.append(random.randint(1, 69))

my_numbers.append(random.randint(1, 26))
winning_numbers.append(random.randint(1, 26))

print(f"My Numbers: {my_numbers}")
print(f"Winning Numbers: {winning_numbers}")

# Challenge 3 The Oscars

best_pictures = [
  '2019 - Parasite',
  '2018 - Green Book',
  '2017 - The Shape of Water',
  '2016 - Moonlight',
  '2015 - Spotlight',
  '2014 - Birdman',
  '2013 - 12 Years a Slave',
  '2012 - Argo',
  '2011 - The Artist',
  '2010 - The King\'s Speech'
]

best_pictures.insert(0, "2022 - Everything Everywhere All at Once")
best_pictures.insert(1, "2021 - CODA")
best_pictures.insert(2, "2020 - Nomadland")

print(best_pictures)

# Challenge 4 Split the bill

bill = [13.99, 28.75, 9.99, 9.99, 6.95, 7.45, 16.45, 16.45]

total = 0

for num in bill:
  total += num

my_share = total / 4
print(my_share)

# Challenge 5 DNA

dna_sequence = ['GCT', 'AGC', 'AGG', 'TAA', 'ACT', 'CAT', 'TAT', 'CCC', 'ACG', 'GAA', 'ACC', 'GGA']

item_to_find = "AGG"
item_found = False

for item in dna_sequence:
  if item == item_to_find:
    item_found = True

if item_found == True:
  print("Item Found!")
else:
  print("Item not found.")