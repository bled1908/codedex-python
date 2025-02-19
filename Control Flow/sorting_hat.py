# Write code below 💖

print("Sorting Hat🎩")
print("Welcome Students, Let's sort you to your respective houses!")

gryffindor = ravenclaw = hufflepuff = slytherin = 0

question1 = int(input("Q1) Do you like Dawn or Dusk?\n\t1) Dawn\n\t2) Dusk\n"))
if question1 == 1:
    gryffindor += 1
    ravenclaw += 1
elif question1 == 2:
    hufflepuff += 1
    slytherin += 1
else:
    print("Wrong input.")

question2 = int(input("Q2) When I'm dead, I want people to remember me as:\n\t1) The Good\n\t2) The Great\n\t3) The Wise\n\t4) The Bold\n"))
if question2 == 1:
    Hufflepuff += 2
elif question2 == 2:
    slytherin += 2
elif question2 == 3:
    ravenclaw += 2
elif question2 == 4:
    gryffindor += 2
else:
    print("Wrong input.")
    
question3 = int(input("Q3) Which kind of instrument most pleases your ear?\n\t1) The violin\n\t2) The trumpet\n\t3) The piano\n\t4) The drum\n"))
if question3 == 1:
    slytherin += 4
elif question3 == 2:
    hufflepuff += 4
elif question3 == 3:
    ravenclaw += 4
elif question3 == 4:
    gryffindor += 4
else:
    print("Wrong input.")
    
print("Calculating the results...")
max_value = max(gryffindor, ravenclaw, hufflepuff, slytherin)
if max_value == gryffindor:
    max_value = "Gryffindor"
elif max_value == ravenclaw:
    max_value = "Ravenclaw"
elif max_value == hufflepuff:
    max_value = "Hufflepuff"
elif max_value == slytherin:
    max_value = "Slytherin"
print(f"You belong to... {max_value}")