alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
e_index = alphabet.index('E')
print(f"'E'在字母表中的索引值为:{e_index}")  # 查找某元素在列表内的下标索引

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
alphabet[0] = "A"  # 修改特定下标索引的值
print(f"alphabet被修改为了：{alphabet}")

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
alphabet.insert(1, 'a')  # ‘insert’：在指定下标位置插入单个新元素
print(f"alphabet被插入元素后为：{alphabet}")

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
alphabet.append('H')  # ‘append’：在列表尾部加入单个新元素
print(f"alphabet被插入元素后为：{alphabet}")

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
add_alphabet = ['H', 'I', 'J']
alphabet.extend(add_alphabet)  # ‘extend’：在列表的尾部添加一批新元素
print(f"alphabet被插入元素后为：{alphabet}")

alphabet = ['A', 'B', 'C', 'D','d',  'E', 'F', 'G']
del alphabet[4]
print(f"alphabet被删除元素后为：{alphabet}")  # ’del‘：删除指定下标索引的值

alphabet = ['A', 'B', 'C', 'D', 'd',  'E', 'F', 'G']
d_alphabet = alphabet.pop(4)
print(f"alphabet被删除元素后为：{alphabet}，取出的变量为：{d_alphabet}。")  # 'pop':将列表中的元素取出

alphabet = ['A', 'B', 'C', 'D', 'd', 'd', 'd', 'E', 'F', 'G']
alphabet.remove("d")  # 'remove':删除某元素在列表中的第一个元素值
print(f"alphabet被删除元素，但是没有删干净的结果为：{alphabet}")

alphabet = ['A', 'B', 'C', 'D', 'd', 'd', 'd', 'E', 'F', 'G']
alphabet.clear()  # 'clear':列表全部清空
print(alphabet)

alphabet = ['A', 'B', 'C', 'D', 'd', 'd', 'd', 'E', 'F', 'G']

# 清空元素
mylist = []
