class Archer:
    name = 'Archer'
    damages = {
        'Warrior': 0.5,
        'Mage': 2,
        'Archer': 1
    }
    damage_mage = 2
    damage_arch = 1
    damage_war = 0.5

    def __init__(self, number):
        self.units = number
