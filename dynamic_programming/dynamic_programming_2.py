# derangements, or permutations w/o fixed points
class Santa:
    cache = [1, 0, 1]
    def __call__(self, n):
        if n < len(self.cache):
            return self.cache[n]
        val = (n-1) * (self(n-1) + self(n-2))
        self.cache.append(val)
        return val


class Sum134:
    cache = [1, 1, 1, 2]
    def __call__(self, n):
        if n < len(self.cache):
            return self.cache[n]
        val = self(n-1) + self(n-3) + self(n-4)
        self.cache.append(val)
        return val


def main():
    santa = Santa()
    print(santa(0)) # should be 1
    print(santa(1)) # should be 0
    print(santa(2)) # should be 1
    print(santa(3)) # should be 2
    print(santa(9)) # should be 133496
    
    sum134 = Sum134()
    print(sum134(0)) # should be 1
    print(sum134(1)) # should be 1
    print(sum134(2)) # should be 1
    print(sum134(3)) # should be 2
    print(sum134(4)) # should be 4
    print(sum134(8)) # should be 25


if __name__ == '__main__':
    main()