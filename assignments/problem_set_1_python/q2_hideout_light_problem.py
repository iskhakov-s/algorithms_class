def xor_sum(int_list):
    """[returns xor sum of all values in a list]

    Args:
        int_list ([list[int]]): [list of positive integers]

    Returns:
        [int]: [xor sum of the list]
    """    
    total = 0  # initialize total by zero
    for i in int_list:  # loop over nt_list
        total = total ^ i  # xor sum
    # total = int_list[0] ^ int_list[1] ^ int_list[2] . . .. .. . .....
    return total  # return sum


def change_light(int_list, guess_hideout):
    """[solves the hideout problem]

    Args:
        int_list ([list[int]]): [a list of positive integers, representing the on lights from the 16 total lights]
        guess_hideout ([int]): [the hideout location, in the range of 0-15]

    Returns:
        [int]: [the hideout light that needs to be flipped to allow the police to tell the hideout location]
    """    
    xor_total = xor_sum(int_list)  # call xor_sum to get sum
    return xor_total ^ guess_hideout  # return xor of guess hideout and xor sum


def main():
    print(xor_sum([5, 8, 9]))
    print(change_light([5, 8, 9], 2))

if __name__ == '__main__':
    main()