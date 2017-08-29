class Warrior:
    name = 'Warrior'
    damages = {
        'Warrior': 1,
        'Mage': 0.5,
        'Archer': 2
    }
    damage_mage = 0.5
    damage_arch = 2
    damage_war = 1

    def __init__(self, number):
        self.units = number
