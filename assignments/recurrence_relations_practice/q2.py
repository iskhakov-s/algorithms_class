# T is time complexity using recursion
def T(n):
    if n == 0:
        return 2
    else:
        return 4*T(n - 1) + n

# t is T simplified
def t(n):
    return (22/9)*4**n - 1/3*n - 4/9

def main():
    for i in range(3, 10):
        print(T(i), t(i))

if __name__ == '__main__':
    main()