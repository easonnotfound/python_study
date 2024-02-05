def check(num):  # 定义函数
    print("请配合测量您的体温！\n")
    if num <= 37.5:
        print(f"您的体温是{num}度，体温正常，请进！")
    else:
        print(f"您的体温是{num}度，体温异常，需要隔离！")

# 调用函数，传入实际参数
check(36.6)
check(37.6)
