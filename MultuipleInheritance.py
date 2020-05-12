class MathTeacher:
    def i_teach(self):
        print('I teach Mathematics')


class ScienceTeacher:
    def i_teach(self):
        print("I teach Science")


class Teacher(ScienceTeacher, MathTeacher):
    def i_teach(self):
        MathTeacher.i_teach(self)
        ScienceTeacher.i_teach(self)


suman = Teacher()
suman.i_teach()
print(Teacher.mro())

print(isinstance(suman, Teacher))  # True
print(isinstance(suman, MathTeacher))  # True
print(issubclass(MathTeacher, Teacher))  # False
print(issubclass(Teacher, ScienceTeacher))  # True
print(issubclass(ScienceTeacher, MathTeacher))  # False
