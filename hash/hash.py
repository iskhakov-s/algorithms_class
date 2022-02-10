from typing import Callable


class HashTable:
    def __init__(self, cap=13):
        self.arr = [None]*cap
        self.cap = cap
        self.h = lambda key, it: (((2*key + 1) % cap) + it**2) % cap
	# h is the hash function, using quadratic probing for collisions
    
    def insert(self, key):
        for i in range(self.cap//2):
            # number theory guarantees that indexes will
            # start repeating after half of them are tried
            idx = self.h(key, i)
            if self.arr[idx] is None:
                self.arr[idx] = key
                return f"{key} was inserted in position {idx}"
        return f"{key} was not inserted"

    def find(self, key):
        idx = None
        i = 0
        while i <= self.cap // 2 and (idx is None or self.arr[idx] != key):
            idx = self.h(key, i)
            i += 1
        if self.arr[idx] == key:
            return idx
        return -1
    


def hash_idx(func: Callable, key: int, num_iter: int):
    """[Returns a list of the first num_iter indices checked for a given hash]
    """    
    return [func(key, i) for i in range(num_iter)]



tbl = HashTable()
for key in [81, 22, 32, 49, 29, 74]:
    print(tbl.insert(key))