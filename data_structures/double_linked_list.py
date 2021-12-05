from __future__ import annotations
from typing import Any


class DoubleLink:
    def __init__(self, val: Any = None, prev: DoubleLink = None, next_: DoubleLink = None):
        self.val = val
        self.next = next_
        self.prev = prev

    def __str__(self) -> str:
        return str(self.val)

    def chain(self, *links: DoubleLink):
        prev_link = self
        for link in links:
            if not isinstance(link, DoubleLink):
                raise ValueError('value passed is not a double link')
            prev_link.next = link
            link.prev = prev_link
            prev_link = link


class DoubleLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.size = 0

    def __getitem__(self, index: int) -> DoubleLink:
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
        curr = self.head
        index = 0
        while isinstance(curr, DoubleLink):
            link = curr
            curr = curr.next
            yield index, link
            index += 1

    def iter_back(self):
        curr = self.tail
        index = self.size-1
        while isinstance(curr, DoubleLink):
            link = curr
            curr = curr.prev
            yield index, link
            index -= 1

    def append_head(self, item: Any) -> None:
        was_empty = self.is_empty()
        if was_empty:
            self.head = DoubleLink(item, self.head)
            self.tail = self.head
        else:
            old_head = self.head
            self.head = DoubleLink(item, self.head)
            self.head.chain(old_head)
        self.size += 1

    def append_tail(self, item: Any) -> None:
        if self.head is None:
            self.append_head(item)
            return
        old_tail = self.tail
        self.tail = DoubleLink(item)
        old_tail.chain(self.tail)
        self.size += 1

    def pop(self, index: int = None) -> DoubleLink:
        if self.is_empty():
            raise ValueError('list is empty')
        if self.size == 1:
            rem_link = self.head
            self.head = self.tail = None
            self.size -= 1
            return rem_link

        if index is None:
            index = self.size-1

        if index == 0:
            rem_head = self.head
            self.head = self.head.next
            self.head.prev = None
            self.size -= 1
            return rem_head
        if index == self.size-1:
            rem_tail = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            self.size -= 1
            return rem_tail
        link = self[index]
        link.prev.chain(link.next)
        self.size -= 1
        return link

    def remove(self, item: Any, iter_forward=True) -> int:
        if self.size == 1:
            if self.head.val == item:
                self.head = self.tail = None
                self.size -= 1
                return 0
            return -1
        if self.head.val == item:
            self.head = self.head.next
            self.head.prev = None
            self.size -= 1
            return 0
        if self.tail.val == item:
            self.tail = self.tail.prev
            self.tail.next = None
            self.size -= 1
            return self.size

        if iter_forward:
            link_iter = self.iter_fwd()
        else:
            link_iter = self.iter_back()

        for idx, link in link_iter:
            if item == link.val:
                link.prev.chain(link.next)
                self.size -= 1
                return idx
        return -1

    def index(self, item: Any, iter_forward=True) -> int:
        if iter_forward:
            link_iter = self.iter_fwd()
        else:
            link_iter = self.iter_back()
        for idx, link in link_iter:
            if link.val == item:
                return idx
        return -1

    def insert(self, index: int, item: Any) -> None:
        new_link = DoubleLink(item)
        if index == 0:
            new_link.chain(self.head)
            self.head = new_link
            self.size += 1
            return
        if index == self.size:
            self.tail.chain(new_link)
            self.tail = new_link
            self.size += 1
            return
        old_link = self[index]
        old_link.prev.chain(new_link, old_link)
        self.size += 1


def main():
    dll = DoubleLinkedList()
    for i in range(10):
        dll.append_tail(i*2)
    print(dll, dll.size)
    print(dll.insert(7, 5))
    print(dll, dll.size)


if __name__ == '__main__':
    main()
