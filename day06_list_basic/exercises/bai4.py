#Tạo dictionary chứa thông tin một chiếc điện thoại:tên, hãng, giá, dung lượng → In ra toàn bộ thông tin

phone = {
    "name": "iPhone 15",
    "brand": "Apple",
    "price": 25000000,
    "storage": "128GB"
}

for key, value in phone.items():
    print(key, ":", value)
