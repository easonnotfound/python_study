# while循环：知道循环的结果
# for循环：知道循环的次数 ==遍历/依次取出


name = "it he i ma is a bread of it cast"
alphabet = 0
for x in name:
    if x == 'a':
        alphabet += 1
print(f"名字 {name} 中有 {alphabet} 个‘a’")


# range语句
# range(num) : 从0开始，到num的前一个数字的序列
# range（num1， num2）: 从num1开始，到num2的前一个数字的序列
# range（num1, num2, step) : 从num1开始，到num2前一个数字结束，数字之间的步长，以step（不打出来就是默认为1）为准【step为'0'会报错】
for x in range(0, 3):
    print("你好")

count = 0
for a in range(1, 101):
    if a % 2 == 0:
        count += 1
print(f"一共有 {count} 个偶数。")

# continue  中断所在循环的当次执行，直接进入下一次（临时中断），不会影响接下来的再次循环
for i in range(1, 3):
    print("[1]first blood")
    for j in range(1, 3):
        print("[2]double kill")
        for k in range(1, 3):
            print("[3]triple kill")
            continue  # "k"中的continue下方的[4]quadra kill不会被执行
            print("[4]quadra kill")  # 不会执行，但是会跑到下一次的‘k'循环里，让[3]triple kill执行完两次
        print("\n[5]penta kill\n")  # 会被执行

# break  直接结束所在的循环 （永久中断）
for i in range(1, 3):
    print("[1]first blood")
    for j in range(1, 3):
        print("[2]double kill")
        for k in range(1, 3):
            print("[3]triple kill")
            break  # "k"的for循环全部结束，不会再去跑下一次的“k'的for循环
            print("[4]quadra kill")  # 不会被执行
        print("\n[5]penta kill\n")  # 会被执行


money = 10000

for i in range(1, 21):
    import random
    score = random.randint(1, 10)
    if score < 5:
        print(f"员工{i}绩效分为：{score}，不满足，下一位。")
        continue  # 有continue则不会往下一个if走，（阻止不达标的员工领钱）返回for，重新再来循环

    if money >= 1000:
        money -= 1000
        print(f"员工{i}绩效分为：{score}，满足，公司剩余薪水{money}，下一位。")

    else:
        print(f"金额不足，当前余额：{money}元，不足以发工资，下个月再发放。")
        break  # 没钱，结束整个for循环

# continue：
# 当 continue 语句被执行时，程序会立即跳过当前循环中剩余的代码，直接进入下一次循环。
# continue 通常用于某个条件下不希望执行循环中的部分代码，但仍然想要继续下一次迭代。

# break：
# 当 break 语句被执行时，程序会立即退出当前循环，不再执行循环内未执行的代码，也不再进行后续的迭代。
# break 通常用于在满足某个条件时立即结束循环。
# 总的来说，continue 用于跳过当前迭代中的代码，继续下一次迭代，而 break 用于完全终止循环。