from math import sqrt

# T is time complexity using recursion
def T(n):
    if n == 0:
        return 2
    if n == 1:
        return 3
    else:
        return 6*T(n - 1) + 9*T(n - 2)

# t is T simplified
def t(n):
    coeff_a = 1 + sqrt(2)/4
    base_a = 3 - 3*sqrt(2)
    coeff_b = 1 - sqrt(2)/4
    base_b = 3 + 3*sqrt(2)
    return (coeff_a * base_a**n)  +  (coeff_b * base_b**n)

def main():
    for i in (2,4,5,7):
        print(T(i), t(i))

if __name__ == '__main__':
    main()