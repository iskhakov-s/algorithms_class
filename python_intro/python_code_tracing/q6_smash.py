def smash(s: str) -> list[str]:
    """[converts str to list]

    Args:
        s (str): [a string]

    Returns:
        list[str]: [a list of each char in s]
    """    
    lst = []
    for i in s:
        lst.append(i)
    return lst

def main():
    print(smash('hello')) # ['h', 'e', 'l', 'l', 'o']
    print(smash('I wanna live!')) # ['I', ' ', 'w', 'a', 'n', 'n', 'a', ' ', 'l', 'i', 'v', 'e', '!']
    
if __name__ == '__main__':
    main()