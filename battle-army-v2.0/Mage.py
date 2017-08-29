from Fighter import Fighter
import random


class Mage(Fighter):


    def __init__(self):
        self.hit_dice = 20
        self.cls = 'Mage'
        health_mod = random.randint(1, 4) * (-1)
        armor_mod = 0
        super().__init__(health_mod, armor_mod)
