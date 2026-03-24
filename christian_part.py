#Christian Burfeind, 

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