# Inheritance allows programmer to create a new class from an existing class. The child class will have all the
# attribute and methods of the parent class


class Teacher:
    def __init__(self, first_name, last_name, students):
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = f"{first_name} {last_name}"
        self.students = students

    def show_details(self):
        print(f"First Name: {self.first_name}\nFull Name: {self.full_name}")
        print(f"Number of students: {self.students}")


class Mathematics(Teacher):
    fav_num = 40


myteachere = Mathematics('Dear', 'John', 30)

myteachere.show_details()
print(myteachere.fav_num)
