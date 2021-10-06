def bad_abbreviate(s: str) -> str:
    """[removes every other char from a str]

    Args:
        s (str): [a string]

    Returns:
        str: [the str with every other letter removed]
    """    
    return s[::2]

def main():
    print(bad_abbreviate('second')) # 'scn'
    print(bad_abbreviate('They called me Mr. Glass.')) # 'Te aldm r ls.'
    
if __name__ == '__main__':
    main()