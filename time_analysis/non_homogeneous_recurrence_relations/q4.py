# T is time complexity using recursion
def T(n):
    if n == 0:
        return 9
    elif n == 1:
        return 10
    elif n == 2:
        return 32
    else:
        return 7*T(n - 2) + 6*T(n - 3)

# t is T simplified
def t(n):
    return -3*(-2)**n + 8*(-1)**n + 4*(3)**n

def main():
    for i in range(3, 10):
        print(T(i), t(i))

if __name__ == '__main__':
    main()