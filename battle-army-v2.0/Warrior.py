import random
from Fighter import Fighter

class Warrior(Fighter):


    def __init__(self):
        self.hit_dice = 10
        self.cls = 'Warrior'
        health_mod = random.randint(1, 10)
        armor_mod = random.randint(1, 6)
        super().__init__(health_mod, armor_mod)
