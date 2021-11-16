def exp10(num: int) -> int:
    """[recursively finds 10 to the power of a positive integer]

    Args:
        num (int): [a positive integer]

    Returns:
        int: [10 to the power of the int]
    """    
    if num == 0:
        return 1
    return 10 * exp10(num-1)

def main():
    print(exp10(3)) # 1000

if __name__ == '__main__':
    main()