a = [3, 1, 1]  # a 是一个列表,列表可变
b = a  # b 只是成为了 a 的一个引用。这意味着 a 和 b 指向内存中的同一个列表
b[0] = 1  # 修改 b[0] = 1 时，实际上也修改了 a 指向的列表
print(a)
print(b)  # 输出相同的结果

a = "AAA"  # a 是一个字符串,字符串在Python中是不可变的（immutable）
b = a  # b 成为 a 的一个引用，但字符串在Python中是不可变的（immutable）
b = 'BBB'  # 创建了一个新的字符串 'BBB' 并让 b 指向它。这不会影响 a 的值
print(a)
print(b)

my_str = "AG超玩会"
index = 0
while index < len(my_str):
    print(my_str[index])
    index += 1
