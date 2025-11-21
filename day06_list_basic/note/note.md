/--------------------------Bài 6: List, Tuple, Set, Dictionary trong Python-------------------/

1. LIST — Danh sách (thay đổi được)
    List dùng để chứa nhiều giá trị.
    Tạo list:
        fruits = ["apple", "banana", "orange"]
    Truy cập phần tử:
        print(fruits[0])  # apple
        print(fruits[2])  # orange
    Thêm phần tử:
        fruits.append("mango")
    Xóa phần tử:
        fruits.remove("banana")
    Duyệt list:
        for item in fruits:
            print(item)

2. TUPLE — Bộ giá trị (không thay đổi được)
    Dùng khi bạn muốn dữ liệu cố định.
        info = ("Tien", 20, "Vietnam")
    Truy cập:
        print(info[0])
    ※ Không thể đổi giá trị:
        info[0] = "Nam" ❌ → lỗi

3. SET — Tập hợp (không chứa phần tử trùng)
    Dùng khi bạn cần loại bỏ giá trị lặp lại.
        numbers = {1, 2, 3, 3, 2}
        print(numbers)   # Kết quả: {1, 2, 3}
    Thêm phần tử:
        numbers.add(4)

4. DICTIONARY — Từ điển (key : value)
    Quan trọng nhất!
    Giống như 1 danh bạ:
        key → tên
        value → số điện thoại
    Ví dụ:
        student = {
            "name": "Tien",
            "age": 20,
            "score": 8.5
        }
    Truy cập:
        print(student["name"])
    Thêm:
        student["address"] = "HCM"
    Sửa:
        student["age"] = 21
    Duyệt dictionary:
        for key, value in student.items():
            print(key, ":", value)



