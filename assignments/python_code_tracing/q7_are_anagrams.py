def are_anagrams(s: str, t: str) -> bool:
    """[checks if the two strings contain the same characters]

    Args:
        s (str): [a string]
        t (str): [a string]

    Returns:
        bool: [if s and t have the same characters True, else False]
    """    
    s_sorted = str(sorted(s))
    t_sorted = str(sorted(t))
    if s_sorted == t_sorted:
        return True
    return False

def main():
    print(are_anagrams('algorithm', 'logarithm')) # True
    print(are_anagrams('test', 'tees')) # False

if __name__ == '__main__':
    main()