import random;

print("Quest for the Celestial Jewel")

print("You awaken as a Vanara warrior, standing before Lord Rama. He tasks you with retrieving the Celestial Jewel, hidden deep within Ravana's fortress. The journey is perilous, and your choices will shape your destiny.")

health = 100       # Player's life points
strength = 10      # Player's physical strength
wisdom = 10        # Player's intelligence for puzzles
faith = 10         # Player's spiritual devotion
has_weapon = False # Tracks if the player has a divine weapon
has_armor = False  # Tracks if the player has celestial armor
success = False    # Tracks if the player has completed the quest

print("Press Enter to begin your adventure...")
input()

print("Act 1: The Forest of Trials")

print('''You find yourself at the edge of a mystical forest. Three paths lie ahead:

1. The River of Reflection (tests your faith).
2. The Cave of Shadows (tests your wisdom).
3. The Cliffs of Valor (tests your strength).''')
print(f"Stats: Health={health}, Strength={strength}, Wisdom={wisdom}, Faith={faith}")
path = int(input("Which path do you choose? (1, 2, 3): "))

# 

if path == 1:
    print("The river shows visions of your deepest fears. You must face these reflections to proceed.")
    print('''Do you:
1. Stare into the water and confront your fears?
2. Avoid the visions and continue forward?
''')
    choice = int(input("What do you do? (1, 2): "))
    if choice == 1:
        print("You face the visions bravely, feeling stronger in your devotion. +5 Faith!")
        faith += 5
    if choice == 2:
        print("The whispers of doubt gnaw at your mind. -10 Health.")
        health -= 10
        
elif path == 2:
    print("The cave is dark and filled with shadowy demons. A voice calls out with a riddle to test your wisdom.")
    print("Answer the riddle: I speak without a mouth and hear without ears. What am I?")
    answer = input("Your answer: ").lower()
    if answer == "echo":
        print("The shadows retreat, leaving a scroll of wisdom. +5 Wisdom!")
        wisdom += 5
    else:
        print("The shadows lash out at you. -10 Health.")
        health -= 10
        
elif path == 3:
    print("You arrive at the base of a massive cliff that juts into the sky. At the top lies a shining treasure—an artifact that can aid you in your journey. However, the cliff is guarded by a Rakshasa eagle, a fearsome demon in the form of a bird. The eagle screeches as it notices your presence, and you must decide how to proceed.")
    print('''Do you:
1. Fight the eagle
2. Sneak past the eagle
''')
    choice = int(input("What do you do? (1, 2): "))
    if choice == 1:
        print("You decide to confront the Rakshasa eagle head-on. This tests your strength.")
        strength += random.randint(1, 6)
        if strength > 15:
            print("You charge at the Rakshasa eagle with unyielding strength, landing a decisive blow. The beast falls, and you claim a piece of celestial armor, imbued with divine energy.")
            has_armor = True
            strength += 10
        else:
            print("The Rakshasa eagle slashes at you with its talons before flying off. You are left wounded but alive.")
            health -= 20
    elif choice == 2:
        print("You decide to avoid a direct confrontation by using stealth. This tests your wisdom.")
        wisdom += random.randint(1, 6)
        if wisdom > 15:
            print("You move silently, blending into the shadows. The eagle doesn’t notice as you slip past, and you ascend the cliff.")
        else:
            print("The eagle spots you and lunges. You narrowly escape but not without injury.")
            health -= 10
            
print("\nAct 2: The Journey Across the Ocean")
print(f"Stats: Health={health}, Strength={strength}, Wisdom={wisdom}, Faith={faith}")
input("Press Enter to continue...")
print("The path through the Forest of Trials has led you to the shores of a vast ocean. The jewel lies deep within Lanka, across these perilous waters. The waves crash violently, and the air hums with dark magic. You must find a way to cross.")

print('''You see three options before you:
      Choices:

1. Call Upon Hanuman (Test Faith)
2. Build a Raft (Test Wisdom)
3. Swim Across (Test Strength)) ''')

choice = int(input("What do you choose? (1, 2, 3): "))

if choice == 1:
    print("You kneel in prayer, calling upon the mighty Hanuman to aid you in this daunting challenge. The winds still, and you sense his divine presence.")
    faith += random.randint(1, 6)
    if faith > 15:
        print("Hanuman appears, lifting you effortlessly across the ocean. You land safely on Lanka’s shores.")
        faith += 5
    else:
        print("Your faith falters, and the ocean rages against you. A massive wave pulls you under, leaving you battered.")
        health -= 15
        
elif choice == 2:
    print("Using your resourcefulness, you gather driftwood and vines to construct a raft. As you push into the water, the waves test your craftsmanship.")
    wisdom += random.randint(1, 6)
    if wisdom > 15:
        print("Your raft holds steady, and you skillfully navigate the treacherous waters to reach Lanka.")
        wisdom += 5
    else:
        print("The waves crash against your raft, breaking it apart. A sea serpent attacks, leaving you injured but alive.")
        health -= 20
        
elif choice == 3:
    print("You take a deep breath and dive into the ocean, trusting in your strength to see you through. The waters are cold and filled with lurking dangers.")
    strength += random.randint(1, 6)
    if strength > 15:
        print("You fend off a lurking shark with a mighty blow and swim to Lanka’s shores, triumphant.")
        strength += 5
    else:
        print("The ocean's currents are too strong, and you are battered by waves. A sea serpent lashes out at you.")
        health -= 25
        
print("\nThe shores of Lanka stretch out before you, and the Fortress of Ravana looms in the distance. You gather your strength and press onward, knowing the jewel lies within.")

print("\nAct 3: The Fortress of Lanka")
print("\nThe Fortress of Lanka is a sprawling maze of towers and guards. Ravana's forces are strong, but the jewel is within reach. You must tread carefully to complete your quest.")

print('''Choices:

1. Sneak Through the Shadows (Test Wisdom)
2. Confront the Guards Head-On (Test Strength)
3. Call Upon Divine Help (Test Faith)''')

choice = int(input("How do you proceed? (1, 2, 3): "))
if choice == 1:
    print("You slip into the shadows, using the cover of darkness to evade the guards. The air is tense, and every step must be precise.")
    wisdom += random.randint(1, 6)
    if wisdom > 15:
        print("You navigate the labyrinth with ease, avoiding detection and reaching the inner sanctum.")
        wisdom += 5
    else:
        print("A guard spots you, and you're forced to flee. You escape but not without injury.")
        health -= 15

elif choice == 2:
    print("You charge into the fortress, battling Ravana's guards with unrelenting strength. The clash of steel echoes through the halls.")
    strength += random.randint(1, 6)
    if strength > 15:
        print("You defeat the guards, clearing a path to the jewel. Their weapons cannot match your might.")
        strength += 5
    else:
        print("The guards overwhelm you. Though you manage to fight them off, you are left injured.")
        health -= 20

elif choice == 3:
    print("You stop in the middle of the fortress, closing your eyes to pray for divine assistance. The heavens answer, and a protective aura surrounds you.")
    faith += random.randint(1, 6)
    if faith > 15:
        print("A divine force guides you through the fortress, bypassing every obstacle with ease.")
        faith += 5
    else:
        print("Your prayers falter as the fortress resists divine intervention. You're forced to find another way, suffering injuries in the process.")
        health -= 10

print("\nThe Final Challenge: Confronting the Shadow Demon")
print(f"Stats: Health={health}, Strength={strength}, Wisdom={wisdom}, Faith={faith}")
input("Press Enter to face the ultimate test...")
print("\nAfter navigating through the Fortress of Lanka, you stand before the inner sanctum. The Celestial Jewel lies on a pedestal, its divine light illuminating the dark chamber. But your path is blocked by a monstrous shadow demon, a guardian of Ravana's magic. The demon roars, its voice shaking the very walls. This is your ultimate test: to retrieve the jewel and fulfill Lord Rama's mission.")  

print('''Choices for the Final Challenge
Engage in Combat (Test Strength)
Outwit the Demon (Test Wisdom)
Invoke Divine Power (Test Faith)
''')

choice = int(input("How do you face the shadow demon? (1, 2, 3): "))

if choice == 1:
    print("You draw your weapon (if you have one) or ready your fists and charge at the demon. Its claws slash at the air, and the room fills with the sound of battle.")
    strength += random.randint(1, 6)
    if strength > 20 or (has_armor and strength > 15):
        print("Your strength overwhelms the demon, landing a decisive blow that dissipates its dark form. The path to the jewel is clear.")
        strength += 10
        print("Congratulations! You have successfully retrieved the Celestial Jewel.")
        success = True
    else:
        print("TThe demon proves too powerful. Though you land some strikes, its claws leave deep wounds before retreating. You stagger forward and grasp the jewel, but at great cost.")
        health -= 30
        
elif choice == 2:
    print("You quickly assess the situation, noticing the demon's reliance on the shadows and its hesitation to approach the light of the Celestial Jewel. You realize that this foe can be defeated with cunning rather than brute force.")
    wisdom += random.randint(1, 6)
    if wisdom > 20:
        print("You trick the demon by luring it into the light of the Celestial Jewel. It writhes and screeches as the divine radiance consumes it. The way is clear.")
        wisdom += 10
        print("Congratulations! You have successfully retrieved the Celestial Jewel.")
        success = True
    else:
        print("Your plan backfires, and the demon launches a vicious counterattack. Injured but determined, you grab the jewel before collapsing to the floor.")
        health -= 25
        
elif choice == 3:
    print("You close your eyes, clutching a talisman gifted by Lord Rama, and pray for divine intervention. The chamber fills with celestial energy as the heavens answer your call.")
    faith += random.randint(1, 6)
    if faith > 20:
        print("A divine beam of light pierces the darkness, striking the shadow demon. It howls as it dissolves into nothingness, leaving the jewel unguarded.")
        faith += 10
        print("Congratulations! You have successfully retrieved the Celestial Jewel.")
        success = True
    else:
        print("Your prayers falter as the demon resists the divine light. You are forced to shield yourself as its dark energy lashes out at you. Injured but resolute, you claim the jewel.")
        health -= 20
        
if success:
    print("You hold the Celestial Jewel in your hands, its divine energy coursing through you. The air around you clears, and the shadow demon is no more. You return to Lord Rama as a hero, your faith, strength, and wisdom proving your worth.")
else:
    print("The shadow demon overpowers you, and darkness consumes the chamber. Your mission ends here, but your sacrifice will not be forgotten.")