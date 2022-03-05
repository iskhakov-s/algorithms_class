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


def paired_counting_sort(vals, ids):
    min_ = min(vals)
    max_ = max(vals)
    dct = {i: 0 for i in range(min_, max_+1)}
    
    # counts the number of each element
    for i in vals:
        dct[i] += 1
    logging.info(str(dct))
    
    # creates a dict with the least indices to sort the ids
    least_idx = {k:0 for k in dct.keys()}
    next_least = 0
    for k, v in dct.items():
        least_idx[k] = next_least
        next_least = v + least_idx[k]
    
    # sorts the ids
    ids2 = ids[:]
    for idx, id_ in enumerate(ids2):
        ids[least_idx[vals[idx]]] = id_
        least_idx[vals[idx]] += 1
        logging.info(str(ids))
    
    # sorts the vals
    idx = 0
    for val, num in dct.items():
        vals[idx:idx+num] = [val] * num
        idx += num
    
    return vals, ids


def main():
    logging.basicConfig(level=logging.INFO)
    # lst = [5,3,2,4,1,7,6,6,3,4,5]
    # print(counting_sort(lst[:]))
    
    scores = [2,3,2,1,4,4,5,2]
    names = ['A','B','C','D','E','F', 'G', 'H']
    print(paired_counting_sort(scores, names))


if __name__ == '__main__':
    main()
    