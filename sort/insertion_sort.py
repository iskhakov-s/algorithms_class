import logging


def insertion_sort(arr):
    for idx in range(1, len(arr)):
 
        key = arr[idx]
        for i in range(idx-1, -1, -1):
            if key < arr[i]:
                arr[i + 1] = arr[i]
            else:
                break
        if i == 0:
            i = -1
        arr[i+1] = key
        logging.info(str(arr))
    return arr


def main():
    logging.basicConfig(level=logging.INFO)
    lst = [5,3,2,4,1]
    print(insertion_sort(lst[:]))


if __name__ == '__main__':
    main()
