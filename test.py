def func(num):
    total = 1
    for i in range(1, num+1):
        total *= (1 - (1/(i+1))**2)
    return total

def fast(num):
    return (num+3)/(2*num+4)

def main():
    for i in range(10, 50):
        print(func(i), fast(i))

if __name__ == '__main__':
    main()