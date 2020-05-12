class MineralWater(object):
    def __init__(self, sodium, calcium):
        self.sodium = sodium
        self.calcium = calcium

    def __eq__(self, other):
        if isinstance(other, MineralWater):
            return self.sodium == other.sodium and self.calcium == other.calcium

        return 'There is a type error'

    def __lt__(self, other):
        if isinstance(other, MineralWater):
            return self.sodium < other.sodium and self.calcium < other.calcium
        return 'There is a type error'

    def __ne__(self, other):
        return not self == other

    def __ge__(self, other):
        return not self < other or self == other

    def __gt__(self, other):
        return not self < other

    def __le__(self, other):
        return self < other or self == other


water1 = MineralWater(32.50, 124)
water2 = MineralWater(32.50, 99)
water3 = MineralWater(32.50, 124)

print(water1 == water3)
print(water1 <= water2)
print(water1 >= water2)
print(water1 < water2)
print(water1 > water2)
print(water1 != water2)
