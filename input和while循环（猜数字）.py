# 猜数字

import random
num = random.randint(1, 100)
count = 0
flag = True
while flag:
    guess_num = int(input("请输入你猜测的数字："))
    count += 1
    if guess_num == num:
        print("恭喜你，猜对啦！")
        flag = False
    else:
        if guess_num > num:
         print("猜的数字太大啦")
        else:
         print("猜的数字太小啦")
print(f"恭喜你猜对啦，一共猜了{count}次，还不错哦。")