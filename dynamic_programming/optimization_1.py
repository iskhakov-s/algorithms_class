def max_link(arr):
    if len(arr) < 2:
        return 0

    return max(sum(arr[:3]) + max_link(arr[4:]), sum(arr[:2]) + max_link(arr[3:]))


if __name__ == '__main__':
    print(max_link([6, 5, 6, 2, 1, 3, 5, 6, 5, 2]))

