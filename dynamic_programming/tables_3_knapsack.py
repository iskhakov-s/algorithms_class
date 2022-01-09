from pprint import pp


def knapsack(max_weight, wts, vals):
    # add a zero for the base case column
    wts = [0] + wts
    vals = [0] + vals
    table = [[0] * (max_weight+1) for _ in wts]
    
    # for every new element iterate up to the given max
    for i, _ in enumerate(wts):
        for w in range(max_weight+1):
            
            # base case for first row/col is 0
            if i == 0 or w == 0:
                table[i][w] = 0
            # if the newest weight can fit in the bag
            # add the potential value of the new sack or keep the old value
            elif wts[i] <= w:
                table[i][w] = max(vals[i] + table[i-1][w-wts[i]], table[i-1][w])
            # otherwise keep the old value
            else:
                table[i][w] = table[i-1][w]
    
    return table[-1][-1], table
  
    
def main():
    wts = [3,4,2,6,7,3,5]
    vals = [7,9,5,12,14,6,12]    
    pp(knapsack(15, wts, vals)[1])


if __name__ == '__main__':
    main()
