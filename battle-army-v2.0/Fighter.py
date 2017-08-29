import random

class Fighter:


    def __init__(self, heald_mod=0, armor_mod=0):
        self.name = self.create_name()
        self.health = 10 + heald_mod
        self.armor = 10 + armor_mod
        self.level = 1


    def create_name(self):
        with open('names.txt') as f:
            names = f.readlines()[0].split(',')
            fname = random.choice(names)
            lname = random.choice(names)
            return fname + ' ' + lname


    def __str__(self):
        return '{0} {1}'.format(self.cls, self.name)
