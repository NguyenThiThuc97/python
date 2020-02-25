# class Animal:
#     name = "Animal"
#     def _getName(self):
#         return (self.name)
# class Chicken(Animal):
#     name = "Chicken"
#     def _getName(self):
#         return self.name
# animal = Animal()
# chicken = Chicken()
# print(animal._getName())
# print(chicken._getName())

# super()
class Animal:
    name = "Animal"
    def _getName(self):
        return (self.name)
class Chicken(Animal):
    name = "Chicken"
    def _getName(self):
        return super().name
animal = Animal()
chicken = Chicken()
print(animal._getName())
print(chicken._getName())
