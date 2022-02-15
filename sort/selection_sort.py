import logging


def selection_sort(arr):
    for idx in range(len(arr)-1, -1, -1):
        max_idx = 0
        for i in range(1, idx+1):
            if arr[i] > arr[max_idx]:
                max_idx = i
        arr[idx], arr[max_idx] = arr[max_idx], arr[idx]
        logging.info(str(arr))
    return arr


def main():
    logging.basicConfig(level=logging.INFO)
    lst = [5,3,2,4,1]
    print(selection_sort(lst[:]))


if __name__ == '__main__':
    main()
