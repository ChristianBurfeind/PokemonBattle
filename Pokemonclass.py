# Josh Eastland
# Pokemon group project

# create the pokemon class

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

