numbers = list(range(3, 13, 4))
print(numbers)

aw = []
for vv in range(1, 11):
    print(vv)
    square = vv ** 2
    aw.append(square)
print(aw)
print(min(aw))
print(max(aw))
print(f"sum(aw)\n")

vvv = [value**2 for value in range(1, 11)]
print(vvv)
