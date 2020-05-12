# Super() Function is used to inherit all instance attribute of parent class as well as new instance attribute for each child class.
# It is used to inherit any method from parent class

class Mobile:
    def __init__(self, mobile_type):
        self.type = mobile_type


class Shop(Mobile):
    def __init__(self, model, price, mobile_type):
        self.model = model
        if int(price) > 0:
            self.price = price
        else:
            price("Price must be positive")
        super().__init__(mobile_type)

    def Details(self):
        print(f'{self.type}')
        print(f'{self.model}')
        print(f'{self.price}')


nokia = Shop('Nokia', '13000', 'Smart Phone')

nokia.Details()
