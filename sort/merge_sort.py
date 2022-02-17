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


def merge(arr, l, m, r):
    l_length = m - l + 1
    r_length = r - m
 
    left = [0] * (l_length)
    right = [0] * (r_length)
 
    for i in range(0, l_length):
        left[i] = arr[l + i]
 
    for j in range(0, r_length):
        right[j] = arr[m + 1 + j]
 
    i = 0    
    j = 0     
    k = l     
 
    while i < l_length and j < r_length:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
 
    while i < l_length:
        arr[k] = left[i]
        i += 1
        k += 1
 
    while j < r_length:
        arr[k] = right[j]
        j += 1
        k += 1
 
 
 
def msort(arr, l, r):
    logging.info(str(arr))
    if l < r:
 
        m = l+(r-l)//2
 
        msort(arr, l, m)
        msort(arr, m+1, r)
        merge(arr, l, m, r)


def main():
    logging.basicConfig(level=logging.INFO)
    lst =  [314, 159, 265, 358, 979, 323, 846, 264, 338, 327, 950, 288, 419, 716]
    print(merge_sort(lst))
    print(msort(lst))


if __name__ == '__main__':
    main()
