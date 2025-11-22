#Tạo hàm bmi(weight, height) → trả về BMI
# → nếu BMI > 25 → "Thừa cân"
# → nếu BMI < 18.5 → "Gầy"
# → còn lại → "Bình thường"
def bmi(weight, height):
    bmi =  weight / (height * height)
    if bmi > 25:
        return "Thừa cân"
    elif bmi < 18.5:
        return "Gầy"
    else:  
        return "Bình Thường"
print(bmi(54,1.5))