import logging


def counting_sort(lst):
    min_ = min(lst)
    max_ = max(lst)
    dct = {i: 0 for i in range(min_, max_+1)}
    
    for i in lst:
        dct[i] += 1
    logging.info(str(dct))
    idx = 0
    for k, v in dct.items():
        lst[idx:idx+v] = [k] * v
        idx += v
    
    return lst


def main():
    logging.basicConfig(level=logging.INFO)
    lst = [5,3,2,4,1,7,6,6,3,4,5]
    print(counting_sort(lst[:]))


if __name__ == '__main__':
    main()