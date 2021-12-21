class Santa:
    table = [1, 0] + [0] * 8
    last_index = 1
    
    def __call__(self, n):
        if n >= self.last_index:
            if n >= len(self.table):
                self.table = self.table[:] +  [0] * (2 * (n-len(self.table)))
            for i in range(self.last_index+1, n+1):
                self.table[i] = (i-1) * (self.table[i-1] + self.table[i-2])
            self.last_index = n
        return self.table[n]
        

class Sum134:
    table = [1, 1, 1, 2] + [0] * 6
    last_index = 3
    
    def __call__(self, n):
        if n >= self.last_index:
            if n >= len(self.table):
                self.table = self.table[:] + [0] * (2 * (n-len(self.table)))
            for i in range(self.last_index+1, n+1):
                self.table[i] = self.table[i-1] + self.table[i-3] + self.table[i-4]
            self.last_index = n
        return self.table[n]
        
        
def sticker_max(tup):
    vals = {tup[:1]:tup[0], tup[:2]:max(tup[:2]), tup[:3]:tup[0]+tup[2]}
    for i in range(3, len(tup)):
        vals[tup[:i+1]] = max(vals[tup[:i]], vals[tup[:i-1]] + tup[i])
    return vals[tup]


def main():
    santa = Santa()
    sum134 = Sum134()

    print(santa(0)) # should be 1
    print(santa(1)) # should be 0
    print(santa(2)) # should be 1
    print(santa(3)) # should be 2
    print(santa(9)) # should be 133496

    print(sum134(0)) # should be 1
    print(sum134(1)) # should be 1
    print(sum134(2)) # should be 1
    print(sum134(3)) # should be 2
    print(sum134(4)) # should be 4
    print(sum134(8)) # should be 25

    print(sticker_max((6, 1, 1, 3))) # should be 9
    print(sticker_max((4, 1, 2, 10, 9))) # should be 15
    print(sticker_max((1, 2, 3, 4))) # should be 6


if __name__ == '__main__':
    main()