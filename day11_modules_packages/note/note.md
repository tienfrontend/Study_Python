/----------------------------------Bài 11: Modules & Packages trong Python--------------------------/
1. Module là gì?
    Module = 1 file Python (.py) chứa code để tái sử dụng.
    Ví dụ bạn có file math_utils.py:
        def add(a, b):
            return a + b
    Để dùng ở file khác:
        import math_utils
        print(math_utils.add(3, 4))

2. import theo từng hàm
    from math_utils import add
    print(add(10, 5))

3. Module có sẵn của Python
    Python có hàng trăm module dựng sẵn.
    Module random:
        import random
        print(random.randint(1, 10))
    Module math:
        import math
        print(math.sqrt(25))
    Module datetime:
        import datetime
        print(datetime.date.today())

4. Tự tạo module của bạn
    File: greet.py
        def hello(name):
            print("Xin chào", name)
    File: main.py
        import greet
        greet.hello("Tiền")

5. Package là gì?
    Package = thư mục chứa nhiều module → phải có file:
        __init__.py
    Ví dụ cấu trúc:
        myapp/
            __init__.py
            math_utils.py
            string_utils.py
    Dùng package:
        from myapp.math_utils import add
        print(add(5, 2))

6. Package có sẵn (siêu quan trọng)

pip install
Cài thư viện từ internet.
Ví dụ cài thư viện requests:
    pip install requests
Dùng:
    import requests
    res = requests.get("https://api.github.com")
    print(res.status_code)




