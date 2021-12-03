from __future__ import annotations
from typing import Any

SENTINEL = object()


class Link:
    def __init__(self, val: Any = None, next_: Link = None):
        self.val = val
        self.next = next_

    def __str__(self) -> str:
        return str(self.val)


class LinkedList:
    def __init__(self, first_item: Any = SENTINEL) -> None:
        self.head = None
        self.size = 0
        if first_item is not SENTINEL:
            self.append(first_item)

    def __len__(self) -> int:
        return self.size

    def is_empty(self) -> bool:
        return self.head is None

    def __str__(self) -> str:
        if self.is_empty():
            return '[]'
        string = '[ '
        for link in self:
            string += str(link) + ','
        return string[:-2] + ' ]'

    def __getitem__(self, index: int) -> Link:
        for count, link in enumerate(self):
            if count == index:
                return link

    def __iter__(self):
        self.curr = self.head
        return self

    def __next__(self) -> Link:
        if not isinstance(self.curr, Link):
            self.curr = self.head
            raise StopIteration
        link = self.curr
        self.curr = self.curr.next
        return link

    def last(self) -> Link:
        for link in self:
            if isinstance(link, Link) and not isinstance(link.next, Link):
                return link

    def append(self, item: Any) -> None:
        if self.size == 0:
            self.head = Link(item)
            self.size += 1
            return
        new_link = Link(item)
        self.last().next = new_link
        self.size += 1

    def index(self, item: Any) -> int:
        for idx, i in enumerate(self):
            if i.val == item:
                return idx
        return -1

    def insert(self, index: int, item: Any) -> None:
        next_ = self[index]
        link = Link(item, next_)
        if index == 0:
            self.head = link
        else:
            prev_link = self[index - 1]
            prev_link.next = link
        self.size += 1

    def remove(self, item: Any) -> int:
        if self.head.val == item:
            self.head = self.head.next
            self.size -= 1
            return 0
        for idx, link in enumerate(self):
            if isinstance(link.next, Link) and link.next.val == item:
                new_next = link.next.next
                link.next = new_next
                self.size -= 1
                return idx + 1
        return -1

    def pop(self, index: int) -> Any:
        if index == 0:
            val = self.head.val
            self.head = self.head.next
            return val
        prev_link = self[index - 1]
        val = prev_link.next.val
        new_next = prev_link.next.next
        prev_link.next = new_next
        self.size -= 1
        return val


def main():
    ll = LinkedList()
    print(ll.is_empty())
    for i in (0, 34543, 'dsfgd', "sdf"):
        ll.append(i)
    print(len(ll))
    print(ll.pop(1))
    print(ll.is_empty())


if __name__ == '__main__':
    main()
