# # Bài 1: Xử lý lỗi chia cho 0:
try:
    x = 10 / 0
except:
    print("Lỗi chia cho 0!")

# # Bài 2: Nhập tuổi từ bàn phím, nếu nhập chữ → báo lỗi "Tuổi phải là số!".

try:
    age = int(input("Nhập tuổi: "))
    print("Tuổi của bạn là:", age)
except ValueError:
    print("Tuổi phải là số!")

# # Bài 3:Đọc file abc.txt, nếu không có file → in ra: "File không tồn tại!"

try:
    f = open("abc.txt")
except FileNotFoundError:
    print("File không tồn tại!")

# Bài 4 (thực tế):Viết hàm divide(a, b) → Nếu b = 0 → báo lỗi → Ngược lại trả về kết quả
def divide():
    a = int(input("nhập a:"))
    b = int(input("nhập b:"))
    if b==0:
        print("lỗi")
    else:
        print("số a:",a,"- số b:",b)
divide()
