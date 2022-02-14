from math import gcd, lcm
import logging

"""
Start with a finite sequence a_0, a_1, a_2, a_3, … a_(n-1) of positive integers. 
If possible, choose two indices j < k such that a_j does not divide a_k, 
and replace a_j and a_k by gcd(a_j, a_k) and lcm(a_j, a_k) respectively. 
Repeat this process until it is not possible to continue.
"""


def sequence1(arr):
    for j, _ in enumerate(arr):
        aj = arr[j]
        for k, _ in enumerate(arr[j+1:], j+1):
            ak = arr[k]
            if (ak % aj) == 0:
                continue
            arr[j], arr[k] = gcd(aj, ak), lcm(aj, ak)
            logging.info(arr)
            return sequence1(arr)
    return arr


def sequence2(arr):
    l = len(arr)
    for k in range(l-1, -1, -1):
        ak = arr[k]
        for j in range(k-1, -1, -1):
            aj = arr[j]
            if (ak % aj) == 0:
                continue
            arr[j], arr[k] = gcd(aj, ak), lcm(aj, ak)
            logging.info(arr)
            return sequence2(arr)
    return arr


def main():
    logging.basicConfig(level=logging.INFO)
    lst = [8, 5, 20, 4, 18]
    sequence1(lst[:])
    print()
    sequence2(lst[:])


if __name__ == '__main__':
    main()
    