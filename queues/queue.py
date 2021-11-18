from __future__ import annotations
from typing import Any, Union, Callable
from warnings import warn


class Queue:
    def __init__(self, *items: Any, cap: int = None) -> None:
        """
        initializes a list, which will store the queue, and enqueues any items given

        :param items: optional items to be enqueued
        :param int cap: optional integer limiting size of queue
        """
        self.lst = []
        self.cap = cap
        self.push(*items)

    def __str__(self):
        """
        Returns queue items from last to first as a str
        """
        return str(self.lst)

    def __len__(self):
        """
        Returns length of the queue
        Equivalent to queue.size
        """
        return self.size

    def enqueue(self, *items: Any) -> None:
        """
        Adds items to the back of the queue

        :exception Warning: if adding item would exceed the cap
        :param items: to be added
        """
        for i in items:
            if self.cap is not None and self.size >= self.cap:
                warn(f'item could not be added, cap limit {self.cap} reached')
                break
            self.lst.insert(0, i)
        
    def dequeue(self, num=1) -> Union[Any, list[Any]]:
        """
        Removes the oldest item from the queue

        :exception Warning: if queue doesn't have any items to remove
        :param int num: number of times to dequeue
        :return: the front item, or num front items from back to front of a list
        """
        if self.size < num:
            warn(f'too many dequeues for queue of size {self.size}')
            return
            
        if num == 1:
            return self.lst.pop()

        pop_list = []
        for _ in range(num):
            pop_list.insert(0, self.lst.pop())
        return pop_list
        
    def peek(self, by_oldest = True) -> Any:
        """
        Returns the oldest item from the queue without modification
        """
        if by_oldest:
            return self.lst[-1]
        else:
            return self.lst[0]

    @property
    def size(self) -> int:
        """
        Returns the length of the queue
        """
        return len(self.lst)
    
    def is_empty(self) -> bool:
        """
        Determines if the queue is empty
        """
        return self.size == 0