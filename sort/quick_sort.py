import logging


def quick_sort(arr, lo=0, hi=None):
    if hi is None:
        hi = len(arr) - 1
        
    if len(arr) <= 1 or lo >= hi:
        return arr
    
    logging.info(str(arr))
      
    i = lo - 1
    pivot = arr[hi]
 
    for j in range(lo, hi):
        if arr[j] <= pivot:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
 
    arr[i+1], arr[hi] = arr[hi], arr[i+1]
    pivot = i + 1

    quick_sort(arr, lo, pivot-1)
    quick_sort(arr, pivot+1, hi)
    
    
def main():
    logging.basicConfig(level=logging.INFO)
    print(quick_sort([47, 32, 81, 24, 19, 86, 68, 21, 77, 10]))
    print()
    print(quick_sort([33, 14, 50, 27, 8]))
    

if __name__ == '__main__':
    main()