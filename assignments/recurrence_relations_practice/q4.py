# T is time complexity using recursion
def T(n):
    if n == 0:
        return 2
    if n == 1:
        return 7
    if n == 2:
        return 12
    return -6*T(n - 1) + 12*T(n - 2) - 8*T(n - 3)

# t is T simplified
def t(n):
    return 2*(-7.69464)**n

def main():
    for i in range(3, 10):
        print(T(i), t(i))

if __name__ == '__main__':
    main()