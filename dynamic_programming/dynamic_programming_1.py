# using classes allows me to store the cases across calls
# also allows me to not use global variables
class Tribonacci:
    tribs = [0,1,1]
    
    def __call__(self,idx):
        if idx < len(Tribonacci.tribs):
            return Tribonacci.tribs[idx]
        Tribonacci.tribs.append(self(idx-1) + self(idx-2) + self(idx-3))
        return Tribonacci.tribs[-1]


# would probably be better if it cleared the dict after each call
class StickerMax:
    sticker_tuples = {}
    
    def __call__(self, tup):
        if len(tup) >= 1:
            new_tup = tup[2:]
            if new_tup not in StickerMax.sticker_tuples:
                StickerMax.sticker_tuples[new_tup] = self(new_tup)
            val1 = tup[0] + StickerMax.sticker_tuples[new_tup]
            if len(tup) >= 2:
                new_tup = tup[3:]
                if new_tup not in StickerMax.sticker_tuples:
                    StickerMax.sticker_tuples[new_tup] = self(new_tup)
                val2 = tup[1] + StickerMax.sticker_tuples[new_tup]
            else:
                return val1
        else:
            return 0
        return val1 if val1 > val2 else val2


def main():
    t = Tribonacci()
    print(t(5))  # should be 7
    sticker_max = StickerMax()
    print(sticker_max((6, 1, 1, 3)))  # should be 9
    print(sticker_max((4, 1, 2, 10, 9)))  # should be 15
    print(sticker_max((1, 2, 3, 4)))  # should be 6


if __name__ == '__main__':
    main()