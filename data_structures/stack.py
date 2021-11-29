from __future__ import annotations
from typing import Any, Union, Callable
import logging

from data_structures.static_list import StaticList


# TODO: test, add docs
class Stack(StaticList):
    def push(self, item: Any) -> None:
        self.arr.append(item)
        self.size += 1
        
    def pop(self) -> Any:
        self.size -= 1
        item = self.arr[self.size]
        self.arr[self.size] = None
        return item
        
    def peek(self) -> Any:
        """
        Returns the top item from the stack without modification
        """
        if self.size > 0:
            return self.arr[self.size-1]
        logging.warning('cannot peek, stack is empty')
        
    # TODO: update all below methods: reverse, pairs_match, postfix
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