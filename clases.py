class Person :
    year = 2022
x = Person()
print(x)

class Student:
    def __init__(self, name, year):
        self.name = name
        self.year = year
        eso = 'esosss'
        self.ano = eso

    def Say(self):
     print('hola puto soy', self.name, 'estoy en el ano', self.year)

    def SaySomething(self, eso):
        print(eso)

denis = Student('denis', 2022)
print(type(denis))
denis.SaySomething('eso papu')
