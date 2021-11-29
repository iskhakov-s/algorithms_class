from __future__ import annotations
from typing import Any


class Link:
    def __init__(self, val: Any = None, next_: Link = None):
        self.val = val
        self.next_link = next_

    def __str__(self) -> str:
        return str(self.val)


class LinkedList:
    def __init__(self, first_item: Any = None) -> None:
        self.head = Link(first_item)
        assert isinstance(self.head, Link)
    
    def __len__(self) -> int:
        count = 0
        for _ in self:
            count += 1
        return count
    
    def __str__(self) -> str:
        string = 'LinkedList['
        for link in self:
            string += str(link) + ','
        return string[:-1] + ']'
    
    def __getitem__(self, index: int) -> Link:
        count = 0
        for link in self:
            if count == index:
                return link
            count += 1
    
    def __iter__(self):
        self.curr = self.head
        return self
    
    def __next__(self) -> Link:
        if not isinstance(self.curr, Link):
            self.curr = self.head
            raise StopIteration
        link = self.curr
        self.curr = self.curr.next_link
        assert isinstance(link, Link)
        return link
    
    def last(self) -> Link:
        for link in self:
            if isinstance(link, Link) and not isinstance(link.next_link, Link):
                return link
    
    def append(self, item: Any) -> None:
        new_link = Link(item)
        self.last().next_link = new_link
        
    def index(self, item: Any) -> int:
        idx = 0
        for i in self:
            if i.val == item:
                return idx
            idx += 1
        return -1
        
    def insert(self, index: int, item: Any) -> None:
        next_link = self[index]
        link = Link(item, next_link)
        if index != 0:
            prev_link = self[index-1]
            prev_link.next_link = link


def main():
    ll = LinkedList(5)
    for i in range(5):
        ll.append(i)
        print(ll)
    ll.insert(2, 'df')
    print(ll)


if __name__ == '__main__':
    main()
