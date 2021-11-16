def reverse_list(lst: list) -> list:
    """[reverses a list's elements]

    Args:
        lst (list): [the list]

    Returns:
        list: [the list, reversed]
    """    
    if len(lst) == 0:
        return []
    return [lst[-1]] + reverse_list(lst[0:-1])

def main():
    lst = [5,4,3,6] # [6,3,4,5]
    print(reverse_list(lst))

if __name__ == '__main__':
    main()