from __future__ import annotations
from typing import Any, Callable
from static_list import StaticList


class Queue(StaticList):
    def __init__(self, cap: int = 10) -> None:
        super(Queue, self).__init__(cap)
        self.front = 0
        self.back = 0
        self.is_looped = False

    def __getitem__(self, index: int):
        if index > self.size or index < 0:
            raise ValueError('index out of range')
        index += self.front
        if index > self.cap:
            index -= self.cap
        return self.arr[index]

    def __str__(self):
        if self.is_looped:
            return str(self.arr[self.front:] + self.arr[:self.back])
        else:
            return str(self.arr[self.front:self.back])

    def enqueue(self, item: Any) -> None:
        self.arr[self.back] = item
        self.back += 1
        if self.back == self.cap:
            self.back = 0
            self.is_looped = True
        self.size += 1
        if self.back == self.front:
            self.resize()

    def dequeue(self) -> Any:
        item = self.arr[self.front]
        self.front += 1
        if self.front == self.cap:
            self.front = 0
            self.is_looped = True
        self.size -= 1
        return item

    def peek(self) -> Any:
        return self.arr[self.front]

    def resize(self, func: Callable[[int], int] = lambda x: 2*x, new_cap: int = None) -> None:
        if self.is_looped:
            self.arr = self.arr[self.front:] + self.arr[:self.back] + ([None] * (self.cap-self.size))
        super(Queue, self).resize(func, new_cap)
        self.front = 0
        self.back = self.size - 1
