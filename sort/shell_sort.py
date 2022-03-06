from insertion_sort import insertion_sort
import logging


def shell_sort(arr, increments = (5, 3, 0)):
    for inc in increments:
        if inc == 0:
            inc = len(arr)
            
        for idx in range(0, len(arr), inc):
            max_idx = min(idx + inc, len(arr))
            arr[idx:max_idx] = insertion_sort(arr[idx:max_idx])
        logging.info(f'{arr} with increment {inc}')
    return arr


def main():
    logging.basicConfig(level=logging.INFO)
    lst = [6,5,3,2,4,8,1,7,6]
    print(shell_sort(lst[:]))


if __name__ == '__main__':
    main()