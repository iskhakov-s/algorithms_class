import logging


class Heap:
    def __init__(self, cap=10):
        self.arr = [None] * cap
        self.cap = cap
        self.size = 0

    def __str__(self):
        return str(self.arr[: self.size])

    def add(self, *items):
        for item in items:
            if self.size == self.cap:
                self.arr = self.arr * 2
                self.cap *= 2
            self.arr[self.size] = item
            logging.info(f'Adding {item} to heap at position {self.size}')
            self.upheap(self.size)
            self.size += 1

    def upheap(self, n):
        """Called when an item is inserted to position n.
        Swaps that item up the heap to preserve the size invariant."""
        parent = (n - 1) // 2
        # logging.info(f'{n=} {parent=} {self.arr[n]=} {self.arr[parent]=}')
        while parent >= 0 and self.arr[parent] > self.arr[n]:
            logging.info(f'Node {self.arr[n]} at position {n} is smaller than its parent {self.arr[parent]} at position {parent}')
            self.arr[parent], self.arr[n] = self.arr[n], self.arr[parent]
            logging.info(f'Nodes swapped, new heap: {self}')
            n = parent
            parent = (n - 1) // 2
        return

    def remove(self, *, num_rems=1):
        out = []
        for _ in range(num_rems):
            if self.size == 0:
                return
            self.size -= 1
            self.arr[0], self.arr[self.size] = self.arr[self.size], self.arr[0]
            self.downheap(0)
            out.append(self.arr[self.size])
        return out if num_rems > 1 else out[0]

    def downheap(self, n: int):
        """Called when at a node that may have smaller children.
        Assuming the children are correct subheaps,
        this will fix the size invariant, going down."""
        left = self.arr[2*n+1]
        right = self.arr[2*n+2]
        # precaution to prevent None errors
        if right is None:
            if left is None:
                return
            child: int = left
        else:
            child = min(left, right)
        
        child_idx = 2*n+1 if self.arr[2*n+1] == child else 2*n+2
        if child_idx < self.size and child < self.arr[n]:
            logging.info(f'Node {self.arr[n]} at position {n} is bigger than its child {child} at position {child_idx}')
            logging.debug(f'heap={self}, {child_idx=} {child=} {n=} {self.arr[n]=}')
            self.arr[child_idx], self.arr[n] = self.arr[n], child
            logging.info(f'Nodes swapped, new heap: {self}')
            self.downheap(child_idx)
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
    logging.basicConfig(level=logging.DEBUG)
    heap1 = Heap()
    heap1.add(5, 2, 4)
    print(heap1.remove())
    heap1.add(1,6)
    print(heap1.remove(num_rems=2))
    heap1.add(3)
    print(heap1.remove(num_rems=3))
    # print("should be 2, 1, 4, 3, 5, 6")

    # heap2 = Heap.heapify([1, 5, 3, 6, 7, 4])
    # print(heap2.remove(num_rems=6))
    # print("should be 1, 3, 4, 5, 6, 7")


if __name__ == "__main__":
    main()

