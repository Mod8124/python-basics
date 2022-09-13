class Person:
    def __init__(self, name, year):
        self.name = name
        self.year = year
    def SayMyname(self):
        print('Im', self.name)

class Student(Person):
    pass

class Teacher(Person):
    def __init__(self, name,year, grade):
        Person.__init__(self, name, year)
        self.grade = grade

    def SayGrade(self):
        print(self.grade)

denis = Student('denis', 22)
denis.SayMyname()

elihan = Teacher('eliahn', 18, 22)
elihan.SayGrade()

# super
# just inheritance everything xd
class Director(Person):
    def __init__(self, name,year ,money):
        super().__init__(self, name , year)
