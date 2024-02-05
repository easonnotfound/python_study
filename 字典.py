# 6.1  6.2
dog = {'color': 'black', 'age': 5}
print(dog['color'])
print(dog['age'])
print(dog)
dog['x_position'] = 0
dog['y_position'] = 25
dog['z_position'] = 10
print(dog)
dog['z_position'] = 15
print(dog)
if dog['age'] <= 4:
    adding_age = -5
elif dog['age'] > 6:
    adding_age = 5
else:
    adding_age = 10
dog['age'] += adding_age
print(f"new age:{dog['age']}")

# 6.2.7
dog = {'color': 'green', 'speed': 'slow'}
cat = dog.get('points', 'no point value assigned')
print(cat)

# 6.3
user = {
    'name': 'eason',
    'age': '19',
    'hobby': 'computer games',
    'nationality': 'china',
    'color': 'yellow',
    }
for key, value in user.items():
    print(f"\nkey:{key.title()}")
    print(f"value:{value.title()}")
    print(f"this guy is eason,he's {key} is {value}")

# 创建一个字符串，包含所有键值对
user_info = ""
for key, value in user.items():
    user_info += f"{key.title()}: {value.title()}, "

# 去除最后的逗号和空格
user_info = user_info.rstrip(', ')

# 输出所有键值对
print(f"\nThis guy's info: {user_info}.")

user = {'name': 'John', 'age': 30, 'city': 'New York'}

for key, value in user.items():
    print(f"Key: {key}, Value: {value}")

# 6.3.2
favorite_languages = {'gary': 'python', 'jerry': 'java', 'dragon': 'c++', 'mike': 'python', 'martin': 'ruby'}
friends = ['mike', 'gary', 'martin']
for name, language in favorite_languages.items():
    print(f"Hi {name.title()}")
    if name in friends:
        print(f"{name.title()}, i know you love {language}, is that right ?")

# 使用keys（）确定某人是否做了某事
aw = {'a', 'b', 'c', 'd'
      }
if 'e' not in aw:
    print("e,please call me again !")
