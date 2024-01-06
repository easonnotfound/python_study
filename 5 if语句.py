# 5.2.1
classmates = ['mike', 'martin', 'gary', 'jerry', 'max']
for classmate in classmates:
    if classmate == 'max':
        print(classmate.upper())
    else:
        print(classmate.title())

# 5.2.3
emma = 'mushroom'
if emma != 'anchovies':
    print(f"{emma}is not emma's favourite food")

# 5.2.4  5.2.5
age = 17
if age > 18:
    print("\nwelcome")

elif age < 18 or age == 18:
    print("\nyou are not allowed to play this game")

# 5.2.6  5.2.7
if 'mike' in classmates:
    print("ture")
elif 'emma' not in classmates:
    print('sorry , we do not know for sure')
elif 'dragon' not in classmates:
    print("clear")
else:
    print("that suspicious guy is coming")

car = 'a'
print(f"{car == 'a'}? i predict ture.")
print(car == 'a')

# 5.3.3
age = 12
if age < 4:
    price = 0
elif age < 12:
    price = 10
elif age < 18:
    price = 15
else:
    price = 20
print(f"your admission cost is {price}.")

# 5.4.1
fruit = ['banana', 'apple', 'peach', 'watermelon']
for mission in fruit:
    if mission == 'peach':
        print("sorry,we haven't got this fruit")
    else:
        print(f"adding {mission}.\n")

# 5.4.2
aw = []
if aw:
    for a in aw:
        print(f"adding{aw}")
    print("finished making your pizza")
else:
    print("what do you mean?\n")

# 5.4.3
guys = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
real_guys = ['c', 'd', 'e']
for guy in guys:
    if guy in real_guys:
        print(f"yes,you ae right {guy}.")
    else:
        print(f"no, they aren't real {guy}.")
