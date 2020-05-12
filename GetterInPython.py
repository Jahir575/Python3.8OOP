# Getter is used to reset a instance attribute

class Name:
    def __init__(self, first_name, last_name, balance):
        self.first_name = first_name
        self._last_name = last_name
        self._balance = balance

    @property
    def full_name(self):
        return f"{self.first_name} {self._last_name}"

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if not isinstance(value, int):
            raise TypeError('The balance should be an integer')
        elif value < 0:
            raise ValueError('The balance can not be zero or negative')
        self._balance = value


myname = Name('Jahir', 'Uddin', 300)

myname.balance = 200

print(myname.full_name)
print(myname.balance)
