import logging


def merge_sort(arr, first=True):
    logging.info(str(arr))
    if len(arr) > 1:
        mid = len(arr) // 2
        merge_sort(left:= arr[:mid], False)
        merge_sort(right := arr[mid:], False)
        idx_l = idx_r = idx = 0
        while len(left) > idx_l and len(right) > idx_r:
            if left[idx_l] > right[idx_r]:
                arr[idx] = right[idx_r]
                idx_r += 1
            else:
                arr[idx] = left[idx_l]
                idx_l += 1
            idx += 1
        while idx_l < len(left):
            arr[idx] = left[idx_l]
            idx += 1
            idx_l += 1
        while idx_r < len(right):
            arr[idx] = right[idx_r]
            idx += 1
            idx_r += 1
    if first:
        return arr


def merge_sort2(arr, l, r):
    
    pass


def main():
    logging.basicConfig(level=logging.INFO)
    lst =  [314, 159, 265, 358, 979, 323, 846, 264, 338, 327, 950, 288, 419, 716]
    print(merge_sort(lst))
    print(merge_sort2(lst))


if __name__ == '__main__':
    main()
