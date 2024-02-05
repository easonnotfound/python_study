def add(a, b):
    """
    add函数可以接收2个参数，进行2数相加的功能
    :param a:形参x表示相加的其中一个数字
    :param b:形参y表示相加的另一个数字
    :return:返回值是两数相加的结果
    """
    result = a + b
    return result  # 如果不使用return，则无法使用这个函数的结果（要用变量去接收并使用这个函数）


add(5, 6)
r = add(1, 2)  # 函数返回的值（return result）被储存在‘r'中
print(r)

# none类型


def say_hi():
    print("hello")


result = say_hi()
print(f"无返回值函数，返回的内容是:{result}")
print(f"无返回值函数，返回的内容类型是:{type(result)}")

# none用于if判断


def check_age(age):
    if age > 18:
        return "SUCCESS"
    else:
        return None  # 在if语句中，None等同于False，一般用于在函数中主动返回None，配合if判断做相关处理


result = check_age(16)
if not result:  # if要运行必须条件为true，None相当于False
    print("未成年，不可以进入")

# None用于声明无初始内容的变量
# name = None


def fun_b():
    print("---2---")


def fun_a():
    print("---1---")
    fun_b()
    print("---3---")


fun_a()  # 调用函数fun_a

#  函数中的变量
number = 200  # 全局变量：在函数外去定义的变量


def test_a():
    print(f"test_a:{number}")  # 全局变量在函数内部可以使用


def test_b():
    number = 500  # 局部变量只在函数内部使用，不会影响更高级别的全局变量
    print(f"test_b:{number}")


print(number)  # 全局变量在函数外部可以使用


def test_c():
    global number  # 在函数内声明该变量为全局变量，可以使得该全局变量发生改变
    number = 300
    print(f"test_c:{number}")


test_a()
test_b()
test_c()
print(number)


money = 5000000

name = input("请输入您的姓名")
def query(show_header, amount):
    if show_header:
        print("--------查询余额--------")
    print(f"{name},您的余额剩余{amount}元")


def saving(name, amount):
    print("--------存款操作--------")
    query(False, money + amount)
    return money + amount


def take_money(name, amount):
    print("--------取款操作--------")
    query(False, money - amount)
# 这里的 query(False, money + amount) 和 query(False, money - amount) 将更新后的余额作为参数传递，以确保显示最新的余额信息。
    return money - amount


def main():
    print("--------主菜单--------")
    print(f"{name}您好，欢迎来到银行ITM，请选择操作：")
    print("查询余额\t[输入1]")
    print("存款\t\t[输入2]")
    print("取款\t\t[输入3]")
    print("退出\t\t[输入4]")
    return input("请输入您的选择：")


while True:
    keyboard_input = main()
    if keyboard_input == "1":
        query(True, money)
    elif keyboard_input == "2":
        try:
            num = float(input("您想要存多少钱？请输入："))
            money = saving(name, num)
        except ValueError:
            """
            这段代码尝试将用户输入的字符串转换为浮点数。
            如果用户输入的内容不能被正确转换为浮点数，
            会引发ValueError异常，
            然后程序会跳转到 except ValueError
            块中执行相应的处理，
            即打印错误消息。

            这是一种有效的方式来处理用户输入可能引发的异常，
            确保程序不会因为无效输入而崩溃，
            而是能够优雅地处理这种情况。
            这段代码尝试将用户输入的字符串转换为浮点数。
            如果用户输入的内容不能被正确转换为浮点数，
            会引发 ValueError 异常，
            然后程序会跳转到 except ValueError 块中执行相应的处理，
            即打印错误消息。

            这是一种有效的方式来处理用户输入可能引发的异常，
            确保程序不会因为无效输入而崩溃，
            而是能够优雅地处理这种情况。
            """
            print("请输入有效的数字。")
    elif keyboard_input == "3":
        try:
            num = float(input("您想要取多少钱？请输入："))
            money = take_money(name, num)
        except ValueError:  # ValueError 是 Python 中的一个内建异常类，用于指示数值类型的操作中发生了无效的值。具体而言，当一个函数或操作期望接收一个特定类型的值，但实际接收到的值无法被正确解释为该类型时，就会引发 ValueError。
            print("请输入有效的数字。")
    elif keyboard_input == "4":
        print("程序结束")
        break
    else:
        print("请输入有效的选项。")