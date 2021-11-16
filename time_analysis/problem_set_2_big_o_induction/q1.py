def find_max_row(array2d: list[list[int]]) -> int:
    """[finds the row with the most 1s]

    Args:
        array2d (list[list[int]]): [a set of rows with 1s on the left and 0s everywhere else]

    Returns:
        int: [the index of the row with most 1s, the first one if multiple]
    """
    n = len(array2d)
    if n != len(array2d[0]):
        return -1
    row = col = max_ = 0
    
    while row < n-1 and col < n-1:
        if array2d[row][col] == 1:
            col += 1
            max_ = row
        else:
            row += 1
        print(f'{row=}, {col=}, {max_=}')
    return max_


def main():
    array = [[1,1,0,0,0,0], 
             [1,0,0,0,0,0], 
             [1,1,1,1,0,0], 
             [1,1,0,0,0,0], 
             [1,1,1,1,0,0], 
             [1,1,1,0,0,0]]
    print(find_max_row(array))


if __name__ == '__main__':
    main()