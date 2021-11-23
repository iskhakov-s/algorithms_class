from typing import Any

from static_list import StaticList


# TODO: test
class Array(StaticList):
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

