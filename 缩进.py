numbers = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
for number in numbers:
    print(f"{number.title()},are you kidding me?")
    print(f"{number.title()},how dare you!\n")
    len(numbers)

numbers.reverse()
print(numbers)
numbers.sort()
print(f"{numbers}\n")
print("f{numbers[3].lower()}\n")
numbers.insert(3, 'X')
print(numbers)
print(sorted(numbers))
