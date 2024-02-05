my_str = "万过薪月，员序程马黑，nohtyP学"
result1 = my_str[::-1][9: 14]  # 倒序字符串，切片取出
print(result1)

result2 = my_str[5:10][::-1]  # 先切片取出，再倒序
print(result2)

result3 = my_str.split("， ")[1].replace("来", "")[::-1]  # split分隔"， "，replace替换"来"为""(空）",最后倒序
