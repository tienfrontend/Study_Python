# OOP thực tế: Tính lương nhân viên
# Tạo class Employee với: name, salary
# method calc_year_salary() → trả về salary * 12
# Tạo 2 nhân viên và in ra lương cả năm.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def calc_year_salary(self):
        print("Tên Nhân Viên:", self.name, "- Lương Cả Năm:", self.salary * 12 )
        
nv =[
    Employee("Nguyễn Võ Tiền", 5000000),
    Employee("Bùi Thị Hạ", 7000000),
    Employee("Nguyễn Quốc Hào", 11000000)
]
for Employee in nv:
    Employee.calc_year_salary()