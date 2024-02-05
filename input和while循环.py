# # 7.2.2 让用户选择如何退出
aw = "\nhey guys:"
aw += "\nTell me what do you mean?"
message = ""  # 创建了一个空字符串变量 message，用于存储用户的输入
while message.lower() != "quit":
    message = input(aw)  # input(aw) 中的 aw 是一个提示信息，它会在用户输入之前显示。用户输入的内容将赋给 message。
    if message != 'quit':  # 结束进程时不打印‘quit’
        print(message)


# 7.2.4 使用break退出循环
