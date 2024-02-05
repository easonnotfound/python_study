players = ['mike', 'emma', 'eason', 'gary', 'may']
print(players[1:4])  # 包含索引 1 到 3 的元素
print(players[2])  # 这是一个单个元素，而不是切片，因此没有[]括号。
print(players[:2])  # 输出的是一个切片，包含索引 0 到 1 的元素
print(players[:-2])  # 倒过来数0 1 2  或  包含索引 0 到 -3 的元素，即去掉最后两个元素
print(players[2:])  # 正着数  包含索引 2 到最后的元素
print(players[-2:])  # 包含索引 -2 到最后的元素，即最后两个元素
print()
print(players[::2])  # 从头取到尾，步长为2
print(players[::-1])  # 从头到尾，步长为-1，即倒着取

my_str = "01234567"
print(my_str[::-1])  # 对str进行切片，从头到尾，步长为-1，等同于将序列反转
print(my_str[3:1:-1])  # 从3开始，到1结束（不取1，步长-1（负负得正序）
print(my_str)
for player in players[:3]:
    print(f"here are they:{player.title()}")

volunteers = players[:]
print(volunteers)
for volunteer in volunteers:
    print(f"Now here are them {(volunteer.title())}\n")

aw = (10, 20, 30, 40, 50)
print(aw[0])
print(aw[1])

for ww in aw:
    print(ww)

aw = (70, 80, 90, 100)
print()  # 空一行

for www in aw:
    print(www)

mylist = [21, 25, 21, 23, 22, 20]
mylist.append(31)  # 追加一个数字到列表尾部
mylist.extend([29, 33, 30])  # 将数据容器的内容依次取出，追加到新列表的尾部
mylist.pop(0)  # 取出列表中特定位置的值
print(mylist)
