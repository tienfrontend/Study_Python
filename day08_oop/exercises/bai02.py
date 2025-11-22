# Tạo class Phone với:name, brand, price
# Method: show_info()
# Tạo 1 object và in thông tin.
class Phone:
    def __init__(self, name, brand, price):
        self.name = name
        self.brand = brand
        self.price  = price
    
    def show_info(self):
        print("Tên Điện Thoại:", self.name, "- Nhãn Hàng:", self.brand, "- Giá:", self.price)
s = [
    Phone("Samsung Galaxy S23", "Samsung", 23000000),
    Phone("Iphone 15 Promax", "Apple", 13000000),
    Phone("Oppo 12pro", "Oppo", 15000000)
    ]
for phone in s:
    phone.show_info()