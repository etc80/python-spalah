from Army import Army


print("How first army should be created? (manual or auto)")
choice = input()

army_human = Army(choice)
print('First army of ', army_human.units, 'fighters is ready for battle!')
print('Composition of the army:')
for s in army_human.squads:
    print(s.units, s.name)

army_computer = Army('auto')
print('Second army of ', army_computer.units, 'fighters is ready for battle!')
print('Composition of the army:')
for s in army_computer.squads:
    print(s.units, s.name)

print('Let the battle begin!!!')
army_human.fight(army_computer)
