# TODO
# Create OrcRace class which has following attributes and methods:
#   - class attribute:
#       BATTLE_CRY
#   - instance attributes:
#       name
#       damage
#       health
#       production_cost
#   - instance methods:
#       deal_damage() - the method will print information about dealt damage, name of the unit and use battle cry
#       go_to() - the method accepts two arguments (coordinates) and print the information about unit movement


class OrcRace:
    BATTLE_CRY = 'Hey! Friend'

    def __init__(self, name, damage, health, production_cost):
        self.name = name
        self.damage = damage
        self.health = health
        self.production_cost = production_cost

    def damage_dealt(self):
        print(self.BATTLE_CRY)
        print(f"Unit {self.name} dealt {self.damage} damage ")

    def goto(self, x, y):
        print(f"Unit {self.name} goto {x},{y}")


orc = OrcRace('orc', 20, 20, 10)
troll = OrcRace('troll', 30, 10, 30)
tauren = OrcRace('tauren', 45, 60, 120)

units = []
units.append(orc)
units.append(troll)
units.append(tauren)

for i in units:
    i.damage_dealt()
    i.goto(20,30)