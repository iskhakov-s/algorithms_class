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


def merge_sort2(lst, aux=None, lo=0, hi=None):
    if aux is None:
        aux = [0]*len(lst)
    if hi is None:
        hi = len(lst)
    mid = (lo + hi) // 2
    # Write the base case.
    if (hi-lo) <= 1:
        return
    print(hi)
    # After the completing the base case, uncomment below
    merge_sort2(lst, aux, lo, mid)
    merge_sort2(lst, aux, mid, hi)
    idxa = lst.index(0) # Use the correct initial value of idxa, the index for aux.
    idx1 = lo # Use the correct initial value of idx1, the index for the first half.
    idx2 = mid # Use the correct initial value of idx2, the index for the second half.
    while idx1 < mid or idx2 < hi:
        # "base case": What are the conditions for finishing one of the halves?
        
        # How do you fill in aux?
        if lst[idx2] < lst[idx1] or idx1 >= mid:
            aux[idxa] = lst[idx2]
            idx2 += 1
        else:
            aux[idxa] = lst[idx1]
            idx1 += 1
        idxa += 1
    logging.info(str(lst), str(aux))
    lst[:] = aux[:]



def main():
    logging.basicConfig(level=logging.INFO)
    lst =  [314, 159, 265, 358, 979, 323, 846, 264, 338, 327, 950, 288, 419, 716]
    print(merge_sort(lst))
    print(merge_sort2(lst))


if __name__ == '__main__':
    main()
