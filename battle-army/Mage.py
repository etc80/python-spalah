class Mage:
    name = 'Mage'
    damages = {
        'Warrior': 2,
        'Mage': 1,
        'Archer': 0.5
    }
    damage_war = 2
    damage_arch = 0.5
    damage_mage = 1

    def __init__(self, number):
        self.units = number
