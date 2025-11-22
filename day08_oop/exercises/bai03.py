# Tạo class:
# Animal có method speak()
# Cat kế thừa Animal, có method meow()
# Tạo object Cat và gọi cả 2 method.

class Animal:
    def speak(self):
        print("Động vật phát ra âm thanh")

class cat(Animal):
    def bark(self):
        print("Meow Moew")

d = cat()
d.speak()  # từ class cha
d.bark()   # từ class con
