/----------------------------Bài 10: Exception – Xử lý lỗi trong Python----------------------/

Khi chạy chương trình, đôi khi sẽ gặp lỗi như:
    -Chia cho 0
    -Mở file không tồn tại
    -Người dùng nhập sai dữ liệu
    -Lỗi cú pháp
    -Lỗi logic

Nếu không xử lý, chương trình sẽ dừng lại ngay → rất nguy hiểm.
Python cho bạn công cụ để xử lý lỗi nhẹ nhàng.

1. Cấu trúc try – except
    try:
        # Code có thể gây lỗi
    except:
        # Code chạy khi có lỗi
Ví dụ:
    try:
        n = 10 / 0
    except:
        print("Có lỗi xảy ra rồi!")

2. Bắt lỗi cụ thể
    try:
        x = int("abc")
    except ValueError:
        print("Không thể chuyển abc thành số!")
Các lỗi thường gặp:
    ValueError → nhập sai kiểu
    ZeroDivisionError → chia cho 0
    FileNotFoundError → file không tồn tại

3. finally – luôn chạy, dù có lỗi hay không
    try:
        f = open("data.txt")
    except FileNotFoundError:
        print("Không tìm thấy file")
    finally:
        print("Luôn chạy đoạn này")

4. raise – tự tạo lỗi
    def set_age(age):
        if age < 0:
            raise ValueError("Tuổi không được âm")
        print("Tuổi hợp lệ")

    set_age(-5)

5. Nhiều except trong cùng 1 try
