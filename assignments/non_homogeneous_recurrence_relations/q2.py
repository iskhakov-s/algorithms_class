# T is time complexity using recursion
def T(n):
    if n == 0:
        return 2
    if n == 1:
        return 1
    else:
        return T(n - 1) + 2*T(n - 2) + 2

# t is T simplified
def t(n):
    return (-1/2 * n) * (-2)**n

def main():
    for i in (2,4,5,7):
        print(T(i), t(i))

if __name__ == '__main__':
    main()