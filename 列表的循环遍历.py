def list1_while_func():
    my_list1 = ['a', 'b', 'c']
    index = 0
    while index < len(my_list1):
        element = my_list1[index]
        print(f"列表的元素：{element}")
        index += 1


list1_while_func()


def list2_for_func():
    my_list2 = [1, 2, 3, 4, 5]
    for element in my_list2:
        print(f"列表元素有：{element}")


list2_for_func()
