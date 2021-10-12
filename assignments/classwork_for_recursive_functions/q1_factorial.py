def factorial(num: int) -> int:
    """[finds the factorial of a positive integer]

    Args:
        num (int): [the positive integer]

    Returns:
        int: [the factorial of the int]
    """    
    if num == 0:
        return 1
    return num * factorial(num-1)

def main():
    print(factorial(6)) # 720

if __name__ == '__main__':
    main()