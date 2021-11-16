def base10(lst: list[int]) -> int:
    if len(lst) == 0:
        return 0
    return lst[-1] + 10 * base10(lst[:-1])

def main():
    print(base10([3, 1, 4])) # 314

if __name__ == '__main__':
    main()
    