# Tạo class Student với: Thuộc tính: name, age - Method: in ra thông tin
# Tạo 2 sinh viên và gọi method.
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        print("Tên Sinh Viên:", self.name, "- Tuổi:", self.age)

s1 = Student("Tien", 20)
s2 = Student("Hạ", 21)
s1.introduce()
s2.introduce()
