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
    pass