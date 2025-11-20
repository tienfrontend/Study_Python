/---------------Bài 2: Biến và Kiểu Dữ Liệu trong Python--------------/
1. Biến (Variable) là gì?
Biến giống như một cái “hộp” để lưu trữ dữ liệu.
Ví dụ:

Hộp A chứa số 5

Hộp B chứa chữ "Tiền"

Trong Python: age = 20  -  name = "Tiền"

Ở đây:

age là biến kiểu số

name là biến kiểu chuỗi (string)

2. Quy tắc đặt tên biến
Python không cho đặt tên linh tinh.

❌ Không được:

Bắt đầu bằng số → 1name

Có khoảng trắng → my name

Dùng ký tự lạ → name!!

✔️ Được:

name

my_name

age2

student_name

3. Các kiểu dữ liệu cơ bản
    a. Số nguyên (int)

Dùng cho số không có dấu thập phân: age = 21 - year = 2025
    
    b. Số thực (float)

Dùng cho số có dấu thập phân: height = 1.72 - weight = 59.5

    c. Chuỗi (string)
Là dạng văn bản, luôn trong dấu " " hoặc ' ': name = "Tien" - message = 'Hello Python'

    d. Boolean (True/False)
Kiểu đúng/sai – rất quan trọng trong điều kiện: is_student = True - has_money = False

4. In giá trị ra màn hình

Dùng hàm print(): name = "Tien" - age = 20
print(name)
print(age)
