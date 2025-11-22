/--------------------------Bài 9: File I/O – Đọc và ghi file trong Python------------------/

Python cho phép bạn:
    -Tạo file
    -Ghi dữ liệu vào file
    -Đọc dữ liệu từ file
    -Ghi nối tiếp
    -Xóa file, kiểm tra file tồn tại

1. Ghi file (write)
    with open("data.txt", "w", encoding="utf-8") as f:
        f.write("Xin chào Tiền!\n")
        f.write("Học Python rất vui!")
Chú ý:
    "w" = ghi mới (ghi đè file cũ)
    Nếu file chưa có, Python sẽ tạo file luôn

2. Ghi thêm nội dung (append)
    with open("data.txt", "a", encoding="utf-8") as f:
        f.write("\nDòng mới được thêm nè!")

3. Đọc file (read)
    Đọc toàn bộ file:
        with open("data.txt", "r", encoding="utf-8") as f:
            data = f.read()
            print(data)
    Đọc từng dòng:
        with open("data.txt", "r", encoding="utf-8") as f:
            for line in f:
                print(line.strip())

4. Kiểm tra file tồn tại
    Dùng thư viện os:
        import os

        if os.path.exists("data.txt"):
            print("File tồn tại")
        else:
            print("File không tồn tại")

5. Xóa file
    import os
    os.remove("data.txt")

6. Ứng dụng thực tế: Lưu danh sách sinh viên vào file

    students = ["Tien", "Nam", "Lan"]

    with open("students.txt", "w", encoding="utf-8") as f:
        for s in students:
            f.write(s + "\n")
