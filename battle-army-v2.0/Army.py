from Warrior import Warrior
from Archer import Archer
from Mage import Mage
from SquadCreator import SquadCreator
import random
import time


class Army:


    def __init__(self, owner):
        self.squadcreator = SquadCreator()
        self.squadcreator.register_type('Warrior', Warrior)
        self.squadcreator.register_type('Archer', Archer)
        self.squadcreator.register_type('Mage', Mage)
        self.owner = owner
        self.available_squads = list(self.squadcreator.registry.keys())
        self.total_squads = len(self.available_squads)
        self.units = 0
        self.squads = []
        if owner.lower() == "auto":
            self.create_squad_auto()
        else:
            self.create_army_user()


    def __str__(self):
        if len(self.squads) == 0:
            return 'Noone is in the army yet'
        output = 'Army of ' + self.owner + ' consist of ' + str(self.total_squads) + ' squads:\n'
        for squad in self.squads:
            squad_cls = squad[0].cls if len(squad)>0 else 'Noone'
            output += '{0} {1}s\n'.format(len(squad), squad_cls)
        return output


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
        squad = self.squadcreator.create_squad(sq_type, soldiers)
        self.available_squads.remove(sq_type)
        self.units += soldiers
        return squad


    def create_army_user(self):
        for _ in range(self.total_squads):
            self.squads.append(self.create_squad_user())


    def create_squad_auto(self):
        for i in range(self.total_squads):
            sq = random.choice(self.available_squads)
            if i < 2:
                soldiers = random.randint(0, 100 - self.units)
            else:
                soldiers = 100 - self.units
            squad = self.squadcreator.create_squad(sq, soldiers)
            self.available_squads.remove(sq)
            self.units += soldiers
            self.squads.append(squad)


    def fight(self, another_army):
        if type(self) != type(another_army):
            return 'Something wrong! Types of armies are not same!'
        self.log_file_name = 'battle_log_' + str(round(time.time()))
        with open(self.log_file_name, 'w') as log_file:
            log_file.writelines(self.__str__())
            log_file.writelines(another_army.__str__())
        while True:
            unit_1, unit_2 = None, None
            for i in range(len(self.squads)):
                if len(self.squads[i]) > 0:
                    unit_1 = random.choice(self.squads[i])
                    squad_1 = i
            for i in range(len(another_army.squads)):
                if len(another_army.squads[i]) > 0:
                    unit_2 = random.choice(another_army.squads[i])
                    squad_2 = i
            if(unit_1 is None or unit_2 is None):
                print('Battle is ower!')
                self.analyze_results(unit_1, unit_2)
                break
            else:
                unit_1_damage = random.randint(1, 20) + random.randint(1, unit_1.hit_dice)
                unit_2_damage = random.randint(1, 20) + random.randint(1, unit_2.hit_dice)
                unit_1.health = unit_1.health - (unit_2_damage - unit_1.armor)
                unit_2.health = unit_2.health - (unit_1_damage - unit_2.armor)
                log = '{0} {1} hits {2} {3} for {4} damage. '.format(
                    unit_1.cls, unit_1.name, unit_2.cls, unit_2.name,
                    unit_1_damage
                )
                log += '{0} health become {1} \n'.format(
                    unit_2.name, unit_2.health
                )
                self.log_battle(self.log_file_name, log)
                log = '{0} {1} hits {2} {3} for {4} damage. '.format(
                    unit_2.cls, unit_2.name, unit_1.cls, unit_1.name,
                    unit_2_damage
                )
                log += '{0} health become {1} \n'.format(
                    unit_1.name, unit_1.health
                )
                self.log_battle(self.log_file_name, log)
                if unit_1.health <= 0:
                    log = '{0} {1} died!'.format(unit_1.cls, unit_1.name)
                    self.log_battle(self.log_file_name, log)
                    self.squads[squad_1].remove(unit_1)
                if unit_2.health <= 0:
                    log = '{0} {1} died!'.format(unit_2.cls, unit_2.name)
                    self.log_battle(self.log_file_name, log)
                    another_army.squads[squad_2].remove(unit_2)



    def analyze_results(self, first, second):

        if(first == None and second != None):
            result = 'Second army won!'
        elif(first != None and second == None):
            result = 'First army won!'
        elif(first == None and second == None):
            result = 'Nobody won! Both armies eliminated each other!'
        print(result)
        self.log_battle(self.log_file_name, result)


    def log_battle(self, file_name, log_string):
        with open(file_name, 'a') as f:
            f.writelines(log_string + '\n')
