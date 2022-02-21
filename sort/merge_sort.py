import logging
import math


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


def in_place_merge_sort(lst, lo=0, hi=None):
    if hi is None:
        hi = len(lst)
    mid = (lo+hi)//2
    if hi == lo:
        return
    
    in_place_merge_sort(lst, lo, mid)
    in_place_merge_sort(lst, mid+1, hi)
    
    diff = hi - lo + 1
    while diff > 0:
        diff = 0 if diff <= 1 else int(math.ceil(diff / 2))
        i = lo
        while (i + diff) < hi:
            j = i + diff
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
            i += 1
    logging.info(lst)


def merge_sort_bu(lst):
    n = len(lst)
    aux = [0]*n
    width = 1
    while width < n:
        idxa = lo = 0
        while lo < n:
            idx1 = lo
            idx2 = mid = lo + width
            hi = mid + width
            if hi > n:
                hi = n
            if mid > n:
                mid = n
            while idx1 < mid or idx2 < hi:
                logging.info(str(lst) + ' ' + str(aux))
                if idx1 == mid:
                    aux[idxa] = lst[idx2]
                    idx2 += 1
                elif idx2 >= hi:
                    aux[idxa] = lst[idx1]
                    idx1 += 1
                elif lst[idx1] < lst[idx2]:
                    aux[idxa] = lst[idx1]
                    idx1 += 1
                else:
                    aux[idxa] = lst[idx2]
                    idx2 += 1
                idxa += 1
            lo = hi
        for i in range(n):
            lst[i] = aux[i]
        width *= 2



def main():
    logging.basicConfig(level=logging.INFO)
    lst =  [314, 159, 265, 358, 979, 323, 84, 626, 4338, 327, 950, 288, 419, 716]
    # print(merge_sort(lst))
    in_place_merge_sort(l := lst[:])
    print(l)
    # print(merge_sort_bu(lst))



if __name__ == '__main__':
    main()
