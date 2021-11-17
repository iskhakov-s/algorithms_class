from __future__ import annotations
from typing import Any, Union, Callable


class Stack:
    def __init__(self, *items: Any, cap: int = None) -> None:
        """
        initializes a list, which will store the stack, and pushes any items given

        :param items: optional items to be pushed to the stack
        :param int cap: optional integer limiting size of stack
        """
        self.lst = []
        self.cap = cap
        self.push(*items)

    def __str__(self):
        """
        Returns stack items from left to right, equivalent to bottom to top

        :return: stack as a str
        """
        return str(self.lst)

    def __len__(self):
        """
        Returns length of the stack
        Equivalent to stack.size

        :rtype: int
        :return: length
        """
        return self.size

    def push(self, *items: Any) -> None:
        """
        Adds items to the top of the stack

        :exception IndexError: if pushing item would exceed the cap
        :param items: to be added
        """
        for i in items:
            if self.cap is not None and self.size >= self.cap:
                raise IndexError(f'item could not be added, cap limit {self.cap} reached')
            self.lst.append(i)
        
    def pop(self, num=1) -> Union[Any, list[Any]]:
        """
        Removes the top item from the stack

        :exception IndexError: if stack has no items left
        :param int num: number of times to pop
        :return: the top item, or num top items from top to bottom in a list
        """
        if num == 1:
            try:
                self.lst.pop()
            except IndexError:
                raise IndexError('pop from empty stack')

        pop_list = []
        for i in range(num):
            pop_list.append(self.pop())
        return pop_list
        
    def peek(self) -> Any:
        """
        Returns the top item from the stack without modification
        """
        return self.lst[-1]

    @property
    def size(self) -> int:
        """
        Returns the length of the stack

        :rtype: int
        """
        return len(self.lst)
    
    def is_empty(self) -> bool:
        """
        Determines if the stack is empty

        :rtype: bool
        """
        return True if self.size == 0 else False
        
    @classmethod
    def reverse(cls, stack: Stack):
        """
        Returns a stack with elements in reverse
        Original stack will be destroyed

        :param Stack stack: the stack
        :rtype: Stack
        """
        flipped = cls()
        for _ in range(stack.size):
            flipped.push(stack.pop())
        return flipped
    
    @classmethod
    def pairs_match(cls, stack: Stack, left: Any = '(', right: Any = ')') -> bool:
        """
        Checks if each right item corresponds to a left item in pairs
        Stack will be destroyed

        :param stack: the stack
        :param left: The left item to match, defaults to '('
        :param right: The right item to match, defaults to ')'
        :return: bool
        """
        unmatched_pairs = 0
        for _ in range(stack.size):
            if (x := stack.pop()) == right:
                unmatched_pairs += 1
            elif x == left:
                unmatched_pairs -= 1
            if unmatched_pairs < 0:
                return False
        if unmatched_pairs != 0:
            return False
        return True
    

# TODO - allow string operators instead of calling the function versions
def postfix(*items: Union[float, Callable[[float, float], float]]) -> float:
    """
    Applies simple math expressions in postfix using stacks
    Only supports functions, not math operators like +-*/
    See operator module for word versions of some math operators

    :exception ValueError: if the argument is not a number or function
    :param items: numbers and functions using postfix notation
    :type items: float, function
    :rtype: float
    """
    """[applies simple math expressions in postfix using stacks]

    See operator module for word versions of some math operators
    
    Raises:
        ValueError: [raised if the argument is not a number or function]

    Returns:
        float: [result of the expression]
    """    
    stk = Stack()
    for item in items:
        if isinstance(item, (int, float)):
            stk.push(item)
        elif callable(item):
            num2, num1 = stk.pop(), stk.pop()
            stk.push(item(num1, num2))
        else:
            raise ValueError('argument is not number or function')
    return stk.peek()