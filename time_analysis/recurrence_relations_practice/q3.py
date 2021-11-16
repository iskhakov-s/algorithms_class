# T is time complexity using recursion
def T(n):
    if n == 0:
        return 2
    if n == 1:
        return 5
    else:
        return 3*T(n - 1) + 10*T(n - 2)

# t is T simplified
def t(n):
    return (5/7)*(-2)**n + (9/7)*(5)**n

def main():
    for i in range(3, 10):
        print(T(i), t(i))

if __name__ == '__main__':
    main()