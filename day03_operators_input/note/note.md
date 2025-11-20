/---------------------Bài 3: Toán tử (Operators) trong Python------------------------/
Python có 3 nhóm toán tử chính mà người mới cần biết:

1. Toán tử số học (Arithmetic Operators)
    Dùng cho các phép tính cơ bản:
        | Toán tử | Ý nghĩa              | Ví dụ    | Kết quả |
        | ------- | -------------------- | -------- | ------- |
        | `+`     | Cộng                 | `5 + 2`  | `7`     |
        | `-`     | Trừ                  | `5 - 2`  | `3`     |
        | `*`     | Nhân                 | `5 * 2`  | `10`    |
        | `/`     | Chia                 | `5 / 2`  | `2.5`   |
        | `//`    | Chia lấy phần nguyên | `5 // 2` | `2`     |
        | `%`     | Chia lấy dư          | `5 % 2`  | `1`     |
        | `**`    | Lũy thừa             | `5 ** 2` | `25`    |
    Ví dụ: 
    a = 10
    b = 3
    print(a + b) # kết quả 13
    print(a / b) # kết quả 3.3333333333333335
    print(a // b) # kết quả 3
    print(a % b) # kết quả 1

2. Toán tử so sánh (Comparison Operators)
    Dùng để so sánh → trả về True hoặc False.
        | Toán tử | Ý nghĩa           | Ví dụ    |
        | ------- | ----------------- | -------- |
        | `==`    | bằng              | `a == b` |
        | `!=`    | không bằng        | `a != b` |
        | `>`     | lớn hơn           | `a > b`  |
        | `<`     | nhỏ hơn           | `a < b`  |
        | `>=`    | lớn hơn hoặc bằng | `a >= b` |
        | `<=`    | nhỏ hơn hoặc bằng | `a <= b` |
    Ví dụ:
    x = 5
    y = 10
    print(x > y)   # kết quả False
    print(x < y)   # kết quả True
    print(x == 5)  # kết quả True

3. Toán tử logic (Logical Operators)
    Dùng để kết hợp nhiều điều kiện
        | Toán tử | Ý nghĩa                      | Ví dụ                    |
        | ------- | ---------------------------- | ------------------------ |
        | `and`   | đúng khi **tất cả** đều đúng | `True and True` → `True` |
        | `or`    | đúng khi **ít nhất 1** đúng  | `False or True` → `True` |
        | `not`   | đảo ngược giá trị            | `not True` → `False`     |
    Ví dụ:age = 20
    is_student = True
    print(age > 18 and is_student) # kết quả true
    print(age < 18 or is_student) # kết quả true
    print(not is_student) # kết quả false

