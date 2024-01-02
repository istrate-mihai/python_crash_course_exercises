from random import randint

class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        print('Random number is: ' +  str(randint(1, self.sides)))
