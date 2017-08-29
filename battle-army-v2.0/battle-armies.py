from Army import Army


def main():
    choice = input('Choose which will be the first army? (user or auto): ')
    army_1 = Army(choice)

    choice = input('Choose which will be the second army? (user or auto): ')
    army_2 = Army(choice)

    army_1.fight(army_2)


if __name__ == "__main__":
    # execute only if run as a script
    main()
