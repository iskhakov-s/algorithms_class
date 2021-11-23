from typing import Any, Callable
import logging


# TODO: integrate with static_list
class Array:
    def __init__(self, cap: int = 10):
        self.arr = [None] * cap
        self.cap = cap if cap > 10 else 10
        self.size = 0

    def __getitem__(self, index: int):
        return self.arr[index]

    def __len__(self) -> int:
        return self.size

    def __str__(self) -> str:
        return str(self.arr)

    def append(self, item: Any) -> None:
        """
        adds item to end of the list

        :param item: item to be added
        """
        self.arr[self.size] = item
        self.size += 1

    # does not support negative indices
    def remove(self, index: int) -> Any:
        """
        remove the item at the given index

        :param int index: the index, negative values not yet supported
        :return: the removed item
        """
        if index >= self.size or index < 0:
            raise ValueError('index out of range')
        removed_val = self.arr[index]
        self.arr[index:self.size-1] = self.arr[index+1:self.size]
        self.arr[self.size-1] = None
        self.size -= 1
        return removed_val

    @property
    def size(self) -> int:
        return self._size

    @size.setter
    def size(self, val: int) -> None:
        """
        updates the size

        if the cap is too small, resize the array
        """
        self._size = val
        if self._size >= self.cap:
            self.resize()
        if self._size <= self.cap // 4:
            self.resize_smaller()

    def resize(self, func: Callable[[int], int] = lambda x: 2*x, new_cap: int = None) -> None:
        """
        creates a new list with a new size

        :param Callable func: function to determine a new cap given the old cap
        :param int new_cap: optional parameter for statically setting a new cap
        :return: the new cap
        """
        old_cap = self.cap
        if new_cap is None:
            new_cap = func(self.cap)
        if not isinstance(new_cap, int):
            raise ValueError('new value of cap is not an integer')
        if new_cap < 10:
            logging.warning('new value of cap is less than 10; it will automatically be set to 10')
            new_cap = 10
        if new_cap <= self.size:
            logging.warning('new value of cap is less than size; it will automatically be set to double the size')
            new_cap = self.size * 2

        if new_cap > old_cap:
            self.arr = self.arr[:] + [None] * (new_cap-old_cap)
        elif new_cap < old_cap:
            self.arr = self.arr[:new_cap]

        self.cap = new_cap
        logging.info(f'cap changed from {old_cap} to {new_cap}')

    def resize_smaller(self, func: Callable[[int], int] = lambda x: x // 2):
        self.resize(func)
