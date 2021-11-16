def boards(lst: list[int]) -> int:
    print(lst)
    if len(lst) == 0:
        return 0
    if len(lst) == 1:
        return lst[0]
    return boards(lst[2:] + [lst[0]*lst[1] + lst[0] + lst[1]])

def main():
    print(boards(list(range(1,21))))

if __name__ == '__main__':
    main()