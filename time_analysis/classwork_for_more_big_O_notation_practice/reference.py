# 1
def factorial(num):
    prod = 1
    for fac in range(2, num + 1):
        prod *= fac
    return prod


# 2
import random as r

def trials(num):
    max_num = 6
    count_list = [0]*num
    for _ in range(max_num):
        list_index = r.randrange(num)
        count_list[list_index] += 1
    return count_list


# 3
def draw_square(num):
    for _ in range(num):
        for _ in range(num):
            print("X", end="")
        print()


# 4
def add_to(num):
    total = 0
    for max_num in range(1, num + 1):
        for _ in range(max_num):
            total += 1
    return total


# 5
def middle(num):
    count = 0
    target = 61
    while num != target:
        count += 1
        num = (num + target) // 2
        if num < target:
            num += 1
    return count


# 6
def gcf(num1, num2):
    while num2 != 0:
        num1, num2 = num2, num1 % num2
    return num1
