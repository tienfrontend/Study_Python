/--------------------------Bài 5: Vòng lặp trong Python (for – while)-----------------------------------/

1. Vòng lặp for

Dùng khi bạn muốn lặp một số lần xác định.
    Cấu trúc:
        for biến in tập_hợp:
            # code
    Ví dụ 1: lặp 5 lần
        for i in range(5):
            print("Hello", i) # kết quả Hello 0, Hello 1, Hello 2, Hello 3, Hello 4
    Ví dụ 2: lặp từ 1 đến 5
        for i in range(1, 6):
            print(i) # kết quả 1, 2, 3, 4, 5
    Ví dụ 3: duyệt danh sách
        fruits = ["apple", "banana", "orange"]
        for fruit in fruits:
            print(fruit) # kết quả apple, banana, orange

2. Vòng lặp while

Dùng khi bạn không biết trước số lần lặp, chỉ lặp khi điều kiện còn đúng.
    Cấu trúc:
        while điều_kiện:
            # code
Ví dụ:
    i = 1
    while i <= 5:
        print(i)
        i += 1 # kết quả 1, 2, 3, 4, 5

3. Lệnh break và continue

Dùng để điều khiển vòng lặp.

break → thoát khỏi vòng lặp
    for i in range(10):
        if i == 5:
            break
        print(i)

continue → bỏ qua lần lặp hiện tại, nhảy sang vòng tiếp theo
    for i in range(5):
        if i == 2:
            continue
        print(i)











