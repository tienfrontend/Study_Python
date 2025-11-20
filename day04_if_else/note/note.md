/-------------------------Bài 4: Câu lệnh điều kiện (if – elif – else)-----------------------/
Trong cuộc sống:

Nếu trời mưa → mang áo mưa

Nếu trời nắng → mang kính

Còn lại → ở nhà

Python cũng hoạt động như vậy.

1. Cấu trúc if cơ bản

    if điều_kiện:
     # việc cần làm
    Ví dụ:
        age = 18
        if age >= 18:
            print("Bạn đã đủ 18 tuổi") # kết quả "Bạn đã đủ 18 tuổi"
2. if – else
    if điều_kiện:
    # đúng thì vào đây
    else:
    # sai thì vào đây
    Ví dụ:
    age = 16
    if age >= 18:
        print("Bạn đã đủ tuổi")
    else:
        print("Bạn chưa đủ tuổi") # kết quả "Bạn chưa đủ tuổi"
3. if – elif – else
    Dùng khi có nhiều điều kiện:
        if điều_kiện_1:
            ...
        elif điều_kiện_2:
            ...
        else:
            ...
    Ví dụ: 
    score = 85

    if score >= 90:
        print("Loại A")
    elif score >= 75:
        print("Loại B")
    else:
        print("Loại C") # kết quả " Loại B"
4. Dấu thụt dòng (indentation)
    Rất quan trọng!

    Python không dùng dấu ngoặc { }
    → Mọi đoạn code bên trong if phải thụt vào 4 dấu cách.

    Sai sẽ lỗi ngay.




