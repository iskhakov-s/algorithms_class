def max_number(lst: list) -> int:
    """[finds the max number in the list]

    Args:
        lst (list): [list of numbers]

    Returns:
        int: [max number in the list, or 0 if empty]
    """    
    if len(lst) == 0:
        return 0
    
    max_ = lst[0]
    for i in lst:
        if i > max_:
            max_ = i
    return max_

def main():
    print(max_number([9, 12, 8]))       # 12
    print(max_number([-2, 1, 0]))       # 1
    print(max_number([5, 5, 5, 5, 5]))  # 5
    
if __name__ == '__main__':
    main()