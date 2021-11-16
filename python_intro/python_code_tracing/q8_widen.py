def widen(s: str, lst: list[int]) -> str:
    """[repeats characters in the string by the amount specified in a list]

    Args:
        s (str): [a string]
        lst (list[int]): [a list of positive integers]

    Returns:
        str: [returns a string with repeated characters, or the empty string if the lengths don't match or a number is negative]
    """    
    if len(s) != len(lst):
        return ''
    
    wide_str = ''
    for letter, count in zip(s, lst):
        if count < 0:
            return ''
        wide_str += letter * count
    return wide_str

def main():
    print(widen('cat', [4, 1, 2])) # 'ccccatt'
    print(widen('book', [0, 2, 1, 3])) # 'oookkk'
    print(widen('knob', [1, 2, 3])) # ''
    print(widen('Hello kitty', [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])) # 'HHHelllllooooo kkiiiiiittttttttyyyyy'
    
if __name__ == '__main__':
    main()