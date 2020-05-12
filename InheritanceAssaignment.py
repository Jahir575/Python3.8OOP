class Ship:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

    def deal_damage(self):
        print(f"Unit {self.name} dealt {self.damage} damage")


class BattleShip(Ship):
    def __init__(self, name, damage, special_damage):
        self.special_damage = special_damage
        super().__init__(name, damage)

    def deal_special_damage(self):
        print(f"Unit {self.name} dealt a special damage of {self.special_damage}")


class BigBattleShip(BattleShip):
    def __init__(self, name, damage, special_damage, bomb_damage):
        self.bomb_damage = bomb_damage
        super().__init__(name, damage, special_damage)

    def deal_damage_twice(self):
        print(f"Unit {self.name} dealt {self.special_damage} damage twice")

    def use_bomb(self):
        print(f"Unit {self.name} dealt {self.bomb_damage} damage with a BOMB")


class CargoShip(Ship):
    def __init__(self, name, damage, capacity):
        self.capacity = capacity
        super().__init__(name, damage)

    def transport(self):
        print(f"Unit {self.name} transported {self.capacity} amount of cargo")


myship = Ship('myship', 50)
myship.deal_damage()
print("-------------------------------------")
mybattleship = BattleShip('mybattleship', 75, 100)
mybattleship.deal_damage()
mybattleship.deal_special_damage()
print("-------------------------------------")
mybigbattleship = BigBattleShip('mybigbattleship', 100, 125, 150)
mybigbattleship.deal_damage()
mybigbattleship.deal_damage_twice()
mybigbattleship.use_bomb()
print("-------------------------------------")
mycargoship = CargoShip('mycargoship',75, 1000)
mycargoship.deal_damage()
mycargoship.transport()
