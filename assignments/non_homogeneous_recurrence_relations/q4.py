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
    return (-11/2)*(-1)**n + (12/5)*(-2)**n + (31/10)*(3)**n

def main():
    for i in range(1,9):
        print(T(i), t(i))

if __name__ == '__main__':
    main()