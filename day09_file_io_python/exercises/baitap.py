# Bai 1: Ghi vào file note.txt nội dung: "Hôm nay học Python. File I/O quá dễ!"

with open("note.txt", "w", encoding="utf-8") as f:
    f.write("Hôm nay học Python.\n")
    f.write("File I/O quá dễ!")
# Bài 2: Ghi thêm dòng: "Tiền học rất giỏi!"

with open("note.txt", "a", encoding="utf-8") as f:
    f.write("\nTiền học rất giỏi!")

# Bài 3: Đọc toàn bộ nội dung file và in ra màn hình.

with open("note.txt", "r", encoding="utf-8") as f:
    data = f.read()
    print(data)

# Bài 4: 
# Tạo file users.txt
# Ghi danh sách 5 người bạn vào file
# Sau đó đọc lại file và in từng tên ra.
# gợi ý : friends = ["Nam", "Lan", "Huy", "Khang", "Mai"]

friends = ["Nguyễn Võ Tiền", "Bùi Thị Hạ", "Nguyễn Quốc Hào", "Nguyễn Tiến Tài", "Trương Tấn Nghĩa"]

with open("user.txt", "w", encoding="utf-8") as f:
    f.writelines(name + "\n" for name in friends)

with open("user.txt", "r", encoding="utf-8") as f:
    print(f.read())
