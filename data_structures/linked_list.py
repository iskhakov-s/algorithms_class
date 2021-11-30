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
        self.head = Link(first_item) if first_item is not None else None
    
    def __len__(self) -> int:
        return self.size
    
    def __str__(self) -> str:
        if self.size == 0:
            return 'LinkedList[]'
        string = 'LinkedList['
        for link in self:
            string += str(link) + ','
        return string[:-1] + ']'
    
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
        self.curr = self.curr.next_link
        assert isinstance(link, Link)
        return link
    
    def last(self) -> Link:
        for link in self:
            if isinstance(link, Link) and not isinstance(link.next_link, Link):
                return link
    
    def append(self, item: Any) -> None:
        if self.size == 0:
            self.head = Link(item)
            return
        new_link = Link(item)
        self.last().next_link = new_link
        
    def index(self, item: Any) -> int:
        for idx,i in enumerate(self):
            if i.val == item:
                return idx
        return -1
        
    def insert(self, index: int, item: Any) -> None:
        next_link = self[index]
        link = Link(item, next_link)
        if index != 0:
            prev_link = self[index-1]
            prev_link.next_link = link
    
    def remove(self, item: Any) -> int:
        if self.head.val == item:
            self.head = self.head.next_link
            return 0
        for idx, link in enumerate(self):
            if isinstance(link.next_link, Link) and link.next_link.val == item:
                new_next = link.next_link.next_link
                link.next_link = new_next
                return idx
        return -1
        
    def pop(self, index: int) -> Any:
        if index == 0:
            val = self.head.val
            self.head = self.head.next_link
            return val
        prev_link = self[index-1]
        val = prev_link.next_link.val
        new_next = prev_link.next_link.next_link
        prev_link.next_link = new_next
        return val

    @property
    def size(self) -> int:
        count = 0
        for _ in self:
            count += 1
        return count
        

def main():
    ll = LinkedList()
    print(ll)
    for i in (0,34543,'dsfgd',"sdf"):
        ll.append(i)
    print(ll)
    print(ll.remove('dsfgd'))
    print(ll)


if __name__ == '__main__':
    main()
