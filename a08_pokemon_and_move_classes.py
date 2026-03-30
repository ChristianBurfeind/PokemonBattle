#Christian Burfeind, Isaac Fisher, Josh Eastland, Alan Loyoza

#create a program that simulates a pokemon battle

#Add libraries
import random

#Part 1: Creating Move objects
class Move:
    #Create the constructor with parameters for self, move_name, elemental_type, low_attack_points, and high_attack_points.
    def __init__(self, move_name, elemental_type, low_attack_points, high_attack_points):
        self.move_name = move_name
        self.elemental_type = elemental_type
        self.low_attack_points = low_attack_points
        self.high_attack_points = high_attack_points

    #Create a method called get_info with just self as a parameter. It returns a string that includes all of its variables.
    def get_info(self):
        return (f'{self.move_name} (Type: {self.elemental_type}): {self.low_attack_points} to {self.high_attack_points} Attack Points')

    #Create a method called generate_attack_value, with just self as a parameter. It will generate a random number between the low_attack_points and high_attack_points (inclusive on both ends) and return that value.
    def generate_attack_value(self):
        random_value = random.randint(self.low_attack_points, self.high_attack_points)
        return random_value

# Create 9 Move objects.

# Call the constructor 9 times to store 9 different Move objects in 9 different variables. The values that you can pass into the constructor are given in each row in the table below. The Move Name and Elemental Type must be as shown in the table, but you can put different values for the attack points if you'd like:

# Move Name	Elemental Type	Low Attack Points	High Attack Points
# Tackle	Normal	5	20
oTackle = Move('Tackle','Normal', 5, 20)

# Quick Attack	Normal	6	25
oQuickAttack = Move('Quick Attack','Normal', 6, 25)

# Slash	Normal	10	30
oSlash = Move('Slash','Normal', 10, 30)

# Flamethrower	Fire	5	30
oFlamethrower = Move('Flamethrower','Fire', 5, 30)

# Ember	Fire	10	20
oEmber = Move('Ember','Fire', 10, 20)

# Water Gun	Water	5	15
oWaterGun = Move('Water Gun','Water', 5, 15)

# Hydro Pump	Water	20	25
oHydroPump = Move('Hydro Pump','Water', 20, 25)

# Vine Whip	Grass	10	25
oVineWhip = Move('Vine Whip','Grass', 10, 25)

# Solar Beam	Grass	18	27
oSolarBeam = Move('Solar Beam','Grass', 18, 27)

# Create a list that stores each of the 9 objects in it.
lstMoves = [oTackle, oQuickAttack, oSlash, oFlamethrower, oEmber, oWaterGun, oHydroPump, oVineWhip, oSolarBeam]

# Do a for loop that runs 3 times, and in each iteration, do the following:
for iCount in range(0, 4):
    # Randomly select a Move object from the list you created
    iMove = random.randrange(0, len(lstMoves))
    oMove = lstMoves[iMove]

    # Print out the result of the get_info method of the randomly selected object.
    print()
    print(oMove.get_info())
    
    # Print out Generated attack value:  and then the returned value from running the generate_attack_value method on the randomly selected object.
    print(f"Randomly Generated Attack Value: {oMove.generate_attack_value()}")

    # Then delete the move from the list of moves. This ensures that you won't randomly select the same move twice. If you randomly select the same move twice, the automated tests won't pass.
    lstMoves.remove(oMove)

# After finishing the loop, to add a pause in your program, add this line of code:
# input(“Press enter to continue...)
print()
input('Press enter to continue...')

#Part 2
# Create the constructor with parameters for self, name, elemental_type, and hit_points
class Pokemon:
    def __init__(self, name, elemental_type, hit_points):
        self.name = name
        self.elemental_type = elemental_type
        self.hit_points = hit_points

# Create a method called get_info that returns the name, elemental_type, and hit_points in a string.
    def get_info(self):
        return f"{self.name} - Type: {self.elemental_type} - Hit Points: {self.hit_points}"
    
# Create a method called heal with just self as a parameter. It increases the current value of hit_points by 15 and prints out a message with the Pokémon’s name and what 
# their new value of hit_points are. It should print out the message directly in the method, and not return anything. 
    def heal(self):
        self.hit_points += 15
        print(f"{self.name} has been healed to {self.hit_points} hit points.")

# Create 3 Pokemon objects
# Call the constructor 3 times to create 3 different Pokemon objects stored in 3 different variables. The values that you can pass into the constructor are given in each row in the table below:

# Name	Elemental Type	Hit Points
# Bulbasaur	Grass	60
oBulbasaur = Pokemon('Bulbasaur', 'Grass', 60)

# Charmander	Fire	55
oCharmander = Pokemon('Charmander', 'Fire', 55)

# Squirtle	Water	65
oSquirtle = Pokemon('Squirtle', 'Water', 65)

# Call the get_info method on the object storing the Charmander Pokémon and print out the result
print()
print(oCharmander.get_info())

# Then call the heal method on the same Charmander object
oCharmander.heal()

# Then call the get_info method on the same Charmander object again and print out the result (you should see that the hit_points have increased)
print(oCharmander.get_info())

# Put the 3 Pokemon objects into a list
lstPokemon = (oBulbasaur, oCharmander, oSquirtle)

# Loop through the list and print out the result of get_info on each Pokemon object in the list.
for iPokemon in range (0, 3):
    oPokemon = lstPokemon[iPokemon]

    print(oPokemon.get_info())