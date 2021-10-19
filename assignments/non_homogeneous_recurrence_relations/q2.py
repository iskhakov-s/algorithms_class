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
    return (4/3)*(-1)**n + (5/3)*(2)**n - 1

def main():
    for i in range(2,10):
        print(T(i), t(i))

if __name__ == '__main__':
    main()