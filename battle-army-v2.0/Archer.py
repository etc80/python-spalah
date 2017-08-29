from Fighter import Fighter
import random


class Archer(Fighter):


    def __init__(self):
        self.hit_dice = 12
        self.cls = 'Archer'
        health_mod = random.randint(1, 6)
        armor_mod = random.randint(1, 4)
        super().__init__(health_mod, armor_mod)
