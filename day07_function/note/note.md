/------------------------------Bài 7: Hàm (Function) trong Python-------------------------/

1. Hàm là gì?
    Hàm giống như một “công cụ” bạn tạo ra để làm việc gì đó.
    Ví dụ: Hàm tính tổng, Hàm chào người dùng, Hàm kiểm tra tuổi, Hàm tính BMI
2. Cách tạo hàm trong Python
    Cú pháp:
        def tên_hàm():
            # code
    Ví dụ:
        def say_hello():
            print("Hello Tiền!")
    Gọi hàm:
        say_hello()
3. Hàm có tham số (parameters)
    Nếu muốn truyền dữ liệu vào hàm:
    def greet(name):
        print("Xin chào", name)

    greet("Tiền")
    greet("Lan") # kết quả "Xin chào Tiền", "Xin chào Lan"
4. Hàm có giá trị trả về (return)
    Rất quan trọng!
    def add(a, b):
        return a + b

    result = add(5, 3)
    print(result) # kết quả 8
5. Hàm với nhiều tham số mặc định
    def intro(name="Tiền", age=20):
        print(name, "-", age)

    intro()
    intro("Nam", 25) # kết quả "Tiền - 20, Nam - 25
6. Hàm dùng return để xử lý logic
    def check_age(age):
        if age >= 18:
            return "Đủ tuổi"
        else:
            return "Chưa đủ tuổi"

print(check_age(20)) # Kết quả "Đủ Tuổi"



