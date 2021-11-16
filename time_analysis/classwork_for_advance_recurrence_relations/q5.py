from math import sqrt

# T is time complexity using recursion
def T(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return T(n - 1) + T(n - 2)

# t is T simplified
def t(n):
    a = sqrt(5) / 5
    nphi = (1-sqrt(5))/2
    phi = (1+sqrt(5))/2
    return (-a * nphi**n) + (a * phi**n)

def main():
    for i in (2,4,5,7):
        print(T(i), t(i))

if __name__ == '__main__':
    main()