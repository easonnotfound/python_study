money = 5000000
name = None

name = input("请输入您的姓名")


def query(show_header):
    if show_header:
        print("--------查询余额--------")  # 当show_header为False时，这个if就不会再运行了
    print(f"您的余额剩余{money}元")


def saving(num):
    global money  # money在函数内部定义为全局变量，使得金额在全局改动起作用
    money += num
    print("--------查询余额--------")
    print(f"{name},您存款{num}元成功。")
    query(False)


def take_money(num):
    global money  # money在函数内部定义为全局变量，使得金额在全局改动起作用
    money -= num
    print("--------查询余额--------")
    print(f"{name},您取款{num}元成功，您的余额剩余{money}元")
    query(False)


def main():
    print("--------主菜单--------")
    print(f"{name}您好，欢迎来到银行ATM，请选择操作：")
    print("查询余额\t[输入1]")
    print("存款\t\t[输入2]")
    print("取款\t\t[输入3]")
    print("退出\t\t[输入4]")
    return input("请输入您的选择：")  # return将input的结果


while True:
    keyboard_input = main()
    if keyboard_input == "1":
        query(True)
        continue  # 通过continue继续下一次循环，一进来就回到了主菜单
    elif keyboard_input == "2":
        num = float(input("您想要存多少钱？请输入："))
        saving(num)
        continue
    elif keyboard_input == "3":
        num = float(input("您想要取多少钱？请输入："))
        take_money(num)
        continue
    elif keyboard_input == "4":
        print("程序结束")
        break
    else:
        print("请输入有效的选项。")
