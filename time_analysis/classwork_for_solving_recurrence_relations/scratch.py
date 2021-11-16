from math import log2

def print_tri(num):
    if num == 1:
        print("x")
    else:
        for idx in range(num):
            print("x", end="")
        print()
        print_tri(num - 1)

def mystery_sum(num):
    if num == 0:
        return 0
    total = 0
    for idx1 in range(num):
        for idx2 in range(num):
            total += idx1 * idx2
    return total + mystery_sum(num - 1)

def T(n):
    # print(n)
    if n == 1:
        return 1
    return 1 + 2*T(n-1)

def t(n):
    return 2**(n) - 1

def main():
    test = 15
    print(T(test), t(test))
    
if __name__ == '__main__':
    main()