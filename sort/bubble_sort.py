import logging
from operator import is_


def bubble_sort(arr):
    for end in range(len(arr)-1, -1, -1):
        for i in range(end):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                logging.info(str(arr))
    return arr


def better_bubble(arr):
    for end in range(len(arr)-1, -1, -1):
        is_sorted = True
        for i in range(end):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                logging.info(str(arr))
                is_sorted = False
        if is_sorted:
            break
    return arr


def main():
    logging.basicConfig(level=logging.INFO)
    lst = [5,3,2,4,1]
    print(bubble_sort(lst[:]))
    print(better_bubble(lst[:]))


if __name__ == '__main__':
    main()
