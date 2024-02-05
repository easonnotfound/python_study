i = 1
while i <= 9:
    j = 1
    while j <= i:
        print(f"{i} * {j} = {i * j}\t", end='')  # “end=''”意思是在每一个x输出后不进行任何操作
        j += 1
    i += 1
    print()  # print空内容，让新的循环跳到下一行


# for循环的九九乘法表
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{i} * {j} = {i * j}\t", end='')  # \t可以让生成的内容对齐（制表符）
    # i += 1  在for循环里面不需要
    print()