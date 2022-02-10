import logging


class HashTable:
    DEL = 'deleted'
    
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
            if self.arr[idx] is None or self.arr[idx] == self.DEL:
                self.arr[idx] = key
                logging.info(f"{key} was inserted in position {idx}")
                return 
        logging.info(f"{key} was not inserted")

    def find(self, key):
        idx = None
        i = 0
        while i <= self.cap // 2 and (idx is None or self.arr[idx] != key):
            idx = self.h(key, i)
            i += 1
        if self.arr[idx] == key:
            logging.info(f'{key} found in position {idx}')
            return idx
        logging.info(f'{key} not found')
        return -1

    def delete(self, key):
        idx = self.find(key)
        if idx > 0:
            logging.info(f'{key} deleted from position {idx}')
            self.arr[idx] = self.DEL
        logging.info(f'{key} not deleted')


def hash_idx(func, key, n):
    """[Returns a list of the first n indices checked for a given hash function and key]
    """    
    return [func(key, i) for i in range(n)]


def main():
    logging.basicConfig(level=logging.INFO)  
    tbl = HashTable()
    for key in [81, 22, 32, 49, 29, 74]:
        tbl.insert(key)
    tbl.find(81)
    tbl.find(123432434)
    tbl.delete(81)
    tbl.delete(123432434)
    
if __name__ == '__main__':
    main()