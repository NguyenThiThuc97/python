class Person:
    name = ""
    age = 0
    male = True
    def _setName(self, name):
        self.name = name
    def _getName(self):
        return self.name
    def _setAge(self, age):
        self.age = age
    def _getAge(self):
        return self.age
    def _setMale(self, male):
        self.male = male
    def _getMale(self):
        return self.male
thuc = Person()
thuc._setName("Thuc")
thuc._setAge(23)
print(thuc._getName() + "-" + str(thuc._getAge()))