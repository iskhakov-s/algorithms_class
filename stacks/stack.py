from  __future__ import annotations
from typing import Any, Union, Callable


class Stack:
    def __init__(self, *items: Any) -> None:
        """[initializes a list, which will store the stack, and pushes any items given]
        """             
        self.lst = []
        self.push(*items)
        
    def push(self, *items: Any) -> None:
        """[pushes items to the stack, from left to right]
        """                       
        for i in items:
            self.lst.append(i)
        
    def pop(self) -> Any:
        """[removes the top item from the stack]

        Returns:
            Any: [the top item of the stack]
        """        
        return self.lst.pop()
        
    def peek(self) -> Any:
        """[reveals, but does not remove, the top item of the stack]

        Returns:
            Any: [the top item of the stack]
        """
        return self.lst[-1]
    
    @property
    def size(self) -> int:
        """[returns the number of items in the list]

        Returns:
            int: [the length of the list]
        """        
        return len(self.lst)
    
    def is_empty(self) -> bool:
        """[determines if list is empty]

        Returns:
            bool: [True if empty else False]
        """        
        return True if self.size == 0 else False
        
    @classmethod
    def reverse(cls, stack: Stack):
        """[destroys a stack, and returns its elements in reverse order]

        Args:
            stack (Stack): [the stack to be reversed]

        Returns:
            [type]: [the reversed stack]
        """        
        flipped = cls()
        for _ in range(stack.size):
            flipped.push(stack.pop())
        return flipped
    
    @classmethod
    def pairs_match(cls, stack: Stack, left: str = '(', right: str = ')') -> bool:
        """[checks if each right item corresponds to a left item in pairs]

        Args:
            stack (Stack): [the stack to check for matching]
            left (str, optional): [the left char to be matched]. Defaults to '('.
            right (str, optional): [the right char to be matched]. Defaults to ')'.

        Returns:
            bool: [True if the Items come in pairs, else False]
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