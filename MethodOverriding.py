# Reimplementation of method inherited from base class in the derived class
# It has same name as the method of parent class but can have different attribute
# The implementation in the derived class replaces the implementation of base class

class Computer:
    def __init__(self, name, brand, ram, storage):
        self.name = name
        self.ram = ram
        self.storage = storage
        self.brand = brand

    def Details(self):
        print(f'Name: {self.name}')
        print(f'Brand: {self.brand}')
        print(f'Ram: {self.ram}')
        print(f'Storage: {self.storage}')


class Shop(Computer):
    def __init__(self, name, model, brand, ram, storage):
        self.model = model
        super().__init__(name, brand, ram, storage)

    def Details(self):
        print(f'Name: {self.name}')
        print(f'Brand: {self.brand}')
        print(f'Model: {self.model}')
        print(f'Ram: {self.ram}')
        print(f'Storage: {self.storage}')


nokia = Shop('Mobile', 'Nokia 6.1', 'Nokia', '4', '64' )

nokia.Details()
print("---------------------------------------------")
asus = Computer('Computer', 'brand', 4, 64)

asus.Details()