import logging


def insertion_sort(arr):
    for idx in range(1, len(arr)):
 
        key = arr[idx]
        for i in range(idx-1, -2, -1):
            if i == -1 or key >= arr[i]:
                break
            else:
                arr[i + 1] = arr[i]
        arr[i+1] = key
        logging.info(f'{arr} {key} {i}')
    return arr


def main():
    logging.basicConfig(level=logging.INFO)
    lst = [5,3,2,4,1,7,6]
    print(insertion_sort(lst[:]))


if __name__ == '__main__':
    main()
