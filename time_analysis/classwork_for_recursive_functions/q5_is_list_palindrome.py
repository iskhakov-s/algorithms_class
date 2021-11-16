def is_list_palindrome(lst: list) -> bool:
    """[recursively checks if list is a palindrome]

    Args:
        lst (list): [the list]

    Returns:
        bool: [True if palindrome, else False]
    """    
    print(lst)
    if len(lst) == 0:
        return True
    return (lst[0] == lst[-1]) and is_list_palindrome(lst[1:-1])

def main():
    lst = [5,4,3,6] # False
    print(is_list_palindrome(lst))
    lst = [5,4,3,4,5] # True
    print(is_list_palindrome(lst))

if __name__ == '__main__':
    main()