from __future__ import annotations
from typing import Any


class DoubleLink:
    def __init__(self, val: Any = None, prev: DoubleLink = None, next_: DoubleLink = None) -> None:
        self.val = val
        self.next = next_
        self.prev = prev

    def __str__(self) -> str:
        return str(self.val)

    def chain(self, *links: DoubleLink) -> None:
        """
        Connects the link to the links provided in the arguments

        :param DoubleLink links: DoubleLinks to be chained in order
        """
        prev_link = self
        for link in links:
            if not isinstance(link, DoubleLink):
                raise ValueError('value passed is not a double link')
            prev_link.next = link
            link.prev = prev_link
            prev_link = link


class DoubleLinkedList:
    def __init__(self) -> None:
        # head and tail are sentinel values ie not actually in the list
        self.head = DoubleLink()
        self.tail = DoubleLink()
        self.head.chain(self.tail)
        self.size = 0

    def __getitem__(self, index: int) -> DoubleLink:
        """
        Returns link at index
        Allows negative values, but returns an error for out of range values
        """
        if index < 0:
            index += self.size
        if self.is_closer_to_front(index):
            link_iter = self.iter_fwd()
        else:
            link_iter = self.iter_back()
        for idx, link in link_iter:
            if index == idx:
                return link
        raise ValueError('index out of range')

    def __len__(self) -> int:
        return self.size

    def __str__(self) -> str:
        if self.is_empty():
            return '[]'
        string = '['
        for _, link in self.iter_fwd():
            string += str(link) + ', '
        return string[:-2] + ']'

    def is_empty(self) -> bool:
        return self.head is None

    def is_closer_to_front(self, index: int) -> bool:
        if index <= self.size//2:
            return True
        return False

    def iter_fwd(self):
        """
        Iterates through every key from the link after head up to tail

        :return: A generator that yields the index starting from 0, plus the link
        """
        curr = self.head.next
        index = 0
        while curr is not self.tail:
            link = curr
            curr = curr.next
            yield index, link
            index += 1

    def iter_back(self):
        """
        Iterates through every key from the link before tail back to head

        :return: A generator that yields the index starting from size-1, plus the link
        """
        curr = self.tail.prev
        index = self.size-1
        while curr is not self.head:
            link = curr
            curr = curr.prev
            yield index, link
            index -= 1

    def append_head(self, item: Any) -> None:
        """
        Adds the item as a link to the front
        """
        new_link = DoubleLink(item)
        self.head.chain(new_link, self.head.next)
        self.size += 1

    def append_tail(self, item: Any) -> None:
        """
            Adds the item as a link to the back
            """
        new_link = DoubleLink(item)
        self.tail.prev.chain(new_link, self.tail)
        self.size += 1

    def pop(self, index: int = None) -> DoubleLink:
        """
        Removes the link at the given index

        :return: the link that was removed
        """
        rem_link = self[index]
        rem_link.prev.chain(rem_link.next)
        self.size -= 1
        return rem_link

    def remove(self, item: Any, iter_forward=True) -> int:
        """
        Finds the first link that holds the given item and removes it

        :param item: item to be removed
        :param iter_forward: Boolean determining if it will iterate forwards or backwards to check for the item
        :return: the index of the removed link, or -1 if item was not in the list
        """
        idx = self.index(item, iter_forward)
        if idx == -1:
            return -1
        self.pop(idx)
        return idx

    def index(self, item: Any, iter_forward=True) -> int:
        """
        Finds the index of the given item

        :param item: item to be found
        :param iter_forward: Boolean determining if it will iterate forwards or backwards to check for the item
        :return: the index of the removed link, or -1 if item was not in the list
        """
        if iter_forward:
            link_iter = self.iter_fwd()
        else:
            link_iter = self.iter_back()
        for idx, link in link_iter:
            if link.val == item:
                return idx
        return -1

    def insert(self, index: int, item: Any) -> None:
        """
        Inserts the item as a link at the given position
        """
        new_link = DoubleLink(item)
        old_link = self[index]
        old_link.prev.chain(new_link, old_link)
        self.size += 1


def main():
    dll = DoubleLinkedList()
    for i in range(10):
        dll.append_tail(i*2)
    print(dll, dll.size)
    print(dll.index(14, iter_forward=False))
    print(dll, dll.size)


if __name__ == '__main__':
    main()
