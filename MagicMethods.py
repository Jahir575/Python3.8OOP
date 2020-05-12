class Vehicle(object):
    def __init__(self, milage, owner, brand, model):
        self.milage = milage
        self.owner = owner
        self.brand = brand
        self.model = model

    def show_details(self):
        print(f'Name: {self.__class__.__name__}'
              f'\nMilage: {self.milage}'
              f'\nOwner: {self.owner}'
              f'\nBrand: {self.brand}'
              f'\nModel: {self.model}')

    def __str__(self):
        return ( f'Name: {self.__class__.__name__}'
              f'\nMilage: {self.milage}'
              f'\nOwner: {self.owner}'
              f'\nBrand: {self.brand}'
              f'\nModel: {self.model}')

    def __repr__(self):
        return ( f'Name: {self.__class__.__name__}'
              f'\nMilage: {self.milage}'
              f'\nOwner: {self.owner}'
              f'\nBrand: {self.brand}'
              f'\nModel: {self.model}')

    def __len__(self):
        return 5

class SUV(Vehicle):
    WHEEL = 'Four'

    def show_details(self):
        print(f'Number of Wheel: {self.WHEEL}')
        super(SUV, self).show_details()


duster = SUV(23, 'Jahir', 'Renault', 'Renault Duster')
duster.show_details()
print("-------------------------------------")
print(str(duster))
print("-------------------------------")
print(repr(duster))
print(len(duster))

