class Person():
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def info(self):
        print(self.name)
        print(self.age)
        print(self.city)


misha = Person('Mihail', 18, 'moscow')
misha.info()

print()

oleg = Person('Oleg', 22, 'Piter')
oleg.info()
