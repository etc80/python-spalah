class SquadCreator:
    def __init__(self):
        self.registry = {}


    def register_type(self, name, cls):
        self.registry[name] = cls


    def create_squad(self, cls, units):
        squad = []
        if cls in self.registry:
            for _ in range(units):
                squad.append(self.registry[cls]())
            return squad
        return None
