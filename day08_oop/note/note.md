/-----------------------------Bài 8: Lập trình hướng đối tượng (Class – Object) trong Python-------------------/
1. OOP là gì?
    OOP giúp bạn mô phỏng mọi thứ ngoài đời thật:
    Ví dụ:
        Một học sinh có: Thuộc tính: tên, tuổi, điểm - Hành động: học, ngủ, làm bài
    Trong Python, ta tạo ra một class để mô tả.

2. Class (Lớp)
    Class giống như một cái khuôn mẫu.
    Ví dụ:
        class Student:
            name = "Tien"
            age = 20

3. Object (Đối tượng)
    Object là "sản phẩm" được tạo từ class.
    s = Student()
    print(s.name)
    print(s.age)

4. Hàm init (Constructor)
    Dùng để truyền dữ liệu khi tạo đối tượng.
        class Student:
            def __init__(self, name, age):
                self.name = name
                self.age = age

        s1 = Student("Tien", 20)
        print(s1.name)
        print(s1.age) # kết quả "Tiền - 20"

5. Hàm (method) trong class
    class Student:
        def __init__(self, name, age):
            self.name = name
            self.age = age
        
        def introduce(self):
            print("Tên:", self.name, "- Tuổi:", self.age)

s1 = Student("Tien", 20)
s1.introduce() # kết quả " Tên : Tien - Tuổi : 20"

6. Kế thừa (Inheritance) – Class con kế thừa class cha
    Ví dụ:
        Lớp Animal
        Lớp Dog kế thừa Animal
    class Animal:
        def speak(self):
            print("Động vật phát ra âm thanh")

    class Dog(Animal):
        def bark(self):
            print("Gâu gâu")

d = Dog()
d.speak()  # từ class cha
d.bark()   # từ class con

7. Đóng gói – Tính bảo vệ dữ liệu (Encapsulation)
    class Bank:
        def __init__(self, balance):
            self.__balance = balance  # thuộc tính private

        def get_balance(self):
            return self.__balance

account = Bank(1000)
print(account.get_balance())
