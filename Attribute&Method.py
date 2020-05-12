# Class is a user defined datatype
class Animal:
    WHO_ARE_YOU = 'I am a living being'

    # Attributes: It defines the class. Its unique for each object
    def __init__(self, name, color):  # __init__ method is used to initialize each object. The arguments provided in
        # init method should be provided during declaration of an object too.
        self.name = name
        self.color = color

    def who_are_you(self):  # This is a method. It is same for every object. Every time it is called from any object
        # it will return the same thing.
        print("I am an animal")

    def what_is_your_name(self):
        print(f"My name is {self.name}")

    def what_is_your_color(self):
        print(f"I am {self.color}")


# cat = Animal('Jasper', 'white')
#
# cat.who_are_you()
#
# print(cat.name)
#
# cat.what_is_your_color()

dog = Animal('Hex', 'Black')

dog.what_is_your_color()

dog.what_is_your_name()

print(dog.WHO_ARE_YOU)

print(vars(dog))  # This will print all instance attribute of the class

print(dir(dog))  # This will print all attributes of the class
