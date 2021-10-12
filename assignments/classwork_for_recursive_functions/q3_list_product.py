def list_product(lst: list[int]) -> int:
    """[multiplies the elements of a list]

    Args:
        lst (list[int]): [a list of integers]

    Returns:
        int: [the product of the elements]
    """    
    if len(lst) == 0:
        return 1
    return lst[0] * list_product(lst[1:])

def main():
    lst = [5,4,3,6] # 360
    print(list_product(lst))

if __name__ == '__main__':
    main()