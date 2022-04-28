class Heap:
    def __init__(self, cap=10):
        self.arr = [None]*cap
        self.cap = cap
        self.size = 0
    
    def add(self, item):
        if self.size == self.cap:
            self.arr = self.arr * 2
            self.cap *= 2
        self.arr[self.size] = item
        self.upheap(self.size)
        self.size += 1

    def upheap(self, n):
        """Called when an item is inserted to position n.
        Swaps that item up the heap to preserve the size invariant."""
        
        return

    def remove(self):
        if self.size == 0:
            return
        self.size -= 1
        self.arr[0], self.arr[self.size] = self.arr[self.size], self.arr[0]
        self.downheap(0)
        return self.arr[self.size]

    def downheap(self, n):
        """Called when at a node that may have smaller children.
        Assuming the children are correct subheaps,
        this will fix the size invariant, going down."""
        
        return

    @classmethod
    def heapify(cls, lst):
        """Creates a heap from a given list."""
        heap = cls()
        # Fill in the contents of heap.
        for i in lst:
            heap.add(i)
        return heap


def main():
    heap1 = Heap()
    heap1.add(5)
    heap1.add(2)
    heap1.add(4)
    print(heap1.remove())
    heap1.add(1)
    heap1.add(6)
    print(heap1.remove())
    print(heap1.remove())
    heap1.add(3)
    print(heap1.remove())
    print(heap1.remove())
    print(heap1.remove())
    print("should be 2, 1, 4, 3, 5, 6")

    heap2 = Heap.heapify([1, 5, 3, 6, 7, 4])
    print(heap2.remove())
    print(heap2.remove())
    print(heap2.remove())
    print(heap2.remove())
    print(heap2.remove())
    print(heap2.remove())
    print("should be 1, 3, 4, 5, 6, 7")


if __name__ == "__main__":
    main()
    