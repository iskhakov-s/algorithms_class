# T is time complexity using recursion
def T(n):
    if n == 0:
        return 3
    if n == 1:
        return 6
    else:
        return 2*T(n - 1) + 8*T(n - 2)

# t is T simplified
def t(n):
    return (-2)**n + 2 * 4**n

def main():
    for i in (2,4,5,7):
        print(T(i), t(i))

if __name__ == '__main__':
    main()