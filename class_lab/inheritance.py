class Person:
    name = ""
    age = 0
    male = True

    def __init__(self, name, age, male):
        self.name = name
        self.age = age
        self.male = male

    def _setName(self, name):
        self.name = name
    def _getName(self):
        return self.name

    def _setAge(self, age):
        self.age = age
    def _getAge(self):
        return self.age

    def _setMale(self, male):
        self.name = name
    def _getMale(self):
        return self.male

class Thuc(Person):
    pass
thuc = Thuc("Thuc", 23, False)
print(thuc._getName())