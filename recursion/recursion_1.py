def factorial(num):
    if num == 0:
        return 1
    return num * factorial(num - 1)


def triangle(num):
    print('O' * num)
    if num != 1:
        triangle(num - 1)


def pow2(num):
    if num == 0:
        return 1
    return 2 * pow2(num - 1)


def count(num):
    if num != 0:
        count(num - 1)
    print(num)


if __name__ == '__main__':
    print(factorial(4))  # should be 24
    print(factorial(1))  # should be 1
    print(factorial(0))  # should be 1

    triangle(3)
    # should make
    # OOO
    # OO
    # O

    print(pow2(4))  # should be 16
    print(pow2(1))  # should be 2
    print(pow2(0))  # should be 1

    count(0)  # should be 0
    count(4)  # should be 0, 1, 2, 3, 4 (on different lines)
