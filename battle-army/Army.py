from Warrior import Warrior
from Archer import Archer
from Mage import Mage
import random


class Army:
    units = 0

    def __init__(self, owner):
        self.owner = owner
        self.available_squads = ['Warrior', 'Mage', 'Archer']
        self.units = 0
        self.squads = []
        if owner.lower() == "auto":
            self.create_squad_auto()
        else:
            self.create_army_user()


    def ask_user_for_type(self):
        while True:
            print('Input type of squad to add. Awaiable are:',
                  ','.join(self.available_squads))
            sq_type = input()
            if sq_type.title() in self.available_squads:
                break
            else:
                print('Something wrong! Input valid squad type.')
        return sq_type.title()


    def ask_user_for_units(self):
        soldiers = 0
        while True:
            print('OK, how many guys should be there?',
                  100-self.units,
                  'available')
            try:
                soldiers = int(input())
            except ValueError:
                print('Input valid number!')
                continue
            if soldiers <= 100 - self.units:
                break
        return soldiers


    def create_squad_user(self):
        sq_type = self.ask_user_for_type()
        soldiers = self.ask_user_for_units()
        if sq_type == 'Warrior':
            squad = Warrior(soldiers)
        elif sq_type == 'Archer':
            squad = Archer(soldiers)
        elif sq_type == 'Mage':
            squad = Mage(soldiers)
        self.available_squads.remove(sq_type)
        self.units += soldiers
        return squad


    def create_army_user(self):
        for _ in range(3):
            self.squads.append(self.create_squad_user())


    def create_squad_auto(self):
        for i in range(3):
            sq = random.choice(self.available_squads)
            if i < 2:
                guys = random.randint(0, 100 - self.units)
            else:
                guys = 100 - self.units
            if sq == 'Warrior':
                squad = Warrior(guys)
            elif sq == 'Archer':
                squad = Archer(guys)
            elif sq == 'Mage':
                squad = Mage(guys)
            self.available_squads.remove(sq)
            self.units += guys
            self.squads.append(squad)


    def fight(self, another_army):
        if type(self) != type(another_army):
            return 'Something wrong! Types of armies are not same!'
        while True:
            first_squad_available, second_squad_available = False, False
            for i in range(len(self.squads)):
                if self.squads[i].units > 0:
                    first_squad = self.squads[i]
                    first_squad_available = True
                    break
            for i in range(len(another_army.squads)):
                if another_army.squads[i].units > 0:
                    second_squad = another_army.squads[i]
                    second_squad_available = True
                    break
            if(not first_squad_available or not second_squad_available):
                print('battle over!')
                self.analyze_results(first_squad_available,second_squad_available)
                break
            print('***** round started *****')
            print('first squad is ', first_squad.name)
            print('second squad is ', second_squad.name)
            fsk = first_squad.damages[second_squad.name]
            first_squad_damage = first_squad.units * fsk
            print('first squad damage ', first_squad_damage)
            ssk = second_squad.damages[first_squad.name]
            second_squad_damage = second_squad.units * ssk
            print('second squad damage ', second_squad_damage)
            print('FIGHT!')
            first_squad.units = first_squad.units - second_squad_damage
            second_squad.units = second_squad.units - first_squad_damage
            print('firsts squad units remaining', first_squad.units)
            print('second squad units remaining', second_squad.units)
            print('***** round ended *****')


    def analyze_results(self, first, second):
        if(first == False and second == True):
            print('Second army won!')
        elif(first == True and second == False):
            print('First army won!')
        elif(not first and not second):
            print('Nobody won! Both armies eliminated each other!')
