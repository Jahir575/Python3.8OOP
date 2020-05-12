class OrcRace:
    def __init__(self, name, damage, health):
        self.name = name
        self.damage = damage
        self.health = health

    def deal_damage(self):
        print(f"Unit {self.name} dealt {self.damage} damage")

    def goto(self, x, y):
        print(f"Unit {self.name} went to {x} {y}")


class Troll(OrcRace):
    def throw_spear(self):
        print(f"Unit {self.name} threw spear")
        super().deal_damage()

class Tauren(OrcRace):
    def __init__(self, name, damage, health, special_totem=False):
        self.special_totem = special_totem
        super().__init__(name, damage, health)

    def use_totem(self):
        print(f"The unit {self.name} used totem")
        super().deal_damage()
        if self.special_totem:
            print(f"The unit {self.name} used Special Totem and dealt additional damage")


troll = Troll('Troll', 20, 100)
troll.throw_spear()
troll.goto(45,90)
print("---------------------------------------")
tauren = Tauren('Tauren', 50, 200, True)
tauren.use_totem()

