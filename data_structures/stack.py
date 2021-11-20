from __future__ import annotations
from typing import Any, Union, Callable
from warnings import warn


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
        Returns stack items from bottom to top as a str
        """
        return str(self.lst)

    def __len__(self):
        """
        Returns length of the stack
        Equivalent to stack.size
        """
        return self.size

    def push(self, *items: Any) -> None:
        """
        Adds items to the top of the stack

        :exception Warning: if pushing item would exceed the cap
        :param items: to be added
        """
        for i in items:
            if self.cap is not None and self.size >= self.cap:
                warn(f'item could not be added, cap limit {self.cap} reached')
                break
            self.lst.append(i)
        
    def pop(self, num=1) -> Union[Any, list[Any]]:
        """
        Removes the top item from the stack

        :exception Warning: if stack doesn't have enough items to pop
        :param int num: number of times to pop
        :return: the top item, or num top items from top to bottom in a list
        """
        if self.size < num:
            warn(f'too many pops for stack of size {self.size}')
            return
            
        if num == 1:
            return self.lst.pop()

        pop_list = []
        for _ in range(num):
            pop_list.append(self.lst.pop())
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
        """
        return len(self.lst)
    
    def is_empty(self) -> bool:
        """
        Determines if the stack is empty
        """
        return self.size == 0
        
    @classmethod
    def reverse(cls, stack: Stack):
        """
        Returns a stack with elements in reverse
        Original stack will be destroyed

        :param Stack stack: the stack
        :rtype: Stack
        """
        return cls(*stack.pop(stack.size))
    
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