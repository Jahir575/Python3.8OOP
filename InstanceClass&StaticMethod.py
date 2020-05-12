from datetime import date


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def fromBirthYear(cls, name, birthYear):
        return cls(name, date.today().year - birthYear)

    @staticmethod
    def fromFatherAge(name, fatherAge, fatherAgeDiff):
        return Person(name, date.today().year - fatherAge + fatherAgeDiff)


class Man(Person):
    gender = 'Male'


# Instance Method
person1 = Man('Sahid', 25)
print(isinstance(person1, Man))
print(person1.gender)

print("---------------------------")

# classMethod

person2 = Man.fromBirthYear('John', 1997)
print()
