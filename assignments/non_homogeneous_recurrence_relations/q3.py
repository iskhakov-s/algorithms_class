# T is time complexity using recursion
def T(n):
    if n == 0:
        return 3
    if n == 1:
        return 5
    else:
        return 4*T(n - 1) - 3*T(n - 2) + n

# t is T simplified
def t(n):
    return

def main():
    for i in (2,4,5,7):
        print(T(i), t(i))

if __name__ == '__main__':
    main()