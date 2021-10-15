# T is time complexity using recursion
def T(n):
    if n == 0:
        return 5
    else:
        return 3*T(n - 1)

# t is T simplified
def t(n):
    return 5 * 3 ** n

def main():
    for i in (2,4,5,7):
        print(T(i), t(i))

if __name__ == '__main__':
    main()