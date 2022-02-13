import numpy as np


def levenshtein_price(str1, str2):
    table = [[0 for _ in str2] for _ in str1]

    table[0][0] = 0 if str1[0] == str2[0] else 7
    for i, letter1 in enumerate(str1):
        for j, letter2 in enumerate(str2):
            if i == 0 and j == 0:
                continue

            insert = delete = replace = float('inf')
            if i != 0:
                insert = table[i-1][j] + 8
            if j != 0:
                delete = table[i][j-1] + 3
            if i != 0 and j != 0:
                replace = table[i-1][j-1]
                if str1[i] != str2[j]:
                    replace += 7
            table[i][j] = min(insert, delete, replace)
    return np.array(table)  # inefficient memory-wise but works well for visualization


if __name__ == '__main__':
    print(levenshtein_price('light-crusts-on-cake', 'bite-crusty-uncles'))
