class tribonacci:
    tribs = [0,1,1]
    def __call__(self,idx):
        if idx < len(tribonacci.tribs):
            return tribonacci.tribs[idx]
        tribonacci.tribs.append(self(idx-1) + self(idx-2) + self(idx-3))
        return tribonacci.tribs[-1]