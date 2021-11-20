## 1
### What does each stack operation do?
`size` or `len`: returns the number of items in the stack \
`push`: adds an item to the top of the stack \
`pop`: removes the top item of the stack and returns it \
`is_empty`: returns True if the stack is empty else False \
`peek`: returns the top item of the stack without modifying the stack

## 2
### What are the contents of the stack after the following operations are completed?
| Code               | Result |
|--------------------|--------|
| `stack1 = Stack()` | []     |
| `stack1.push(4)`   | [4]    |
| `stack1.push(6)`   | [4,6]  |
| `stack1.pop()`     | [4]    |
| `stack1.push(8)`   | [4,8]  |
| `stack1.peek()`    | [4,8]  |

The final contents of the stack are [4,8]

## 3
### Describe an algorithm for checking an expression for correctly paired parentheses, using a stack.
See stack.py \
From top to bottom, iterate. If you see a right paren, increment the counter, and if you see a left paren, decrement. If the counter is ever negative, this means there is a left paren with no associated right paren. If the process ends and the counter is not 0, then there is a right paren without a paired left paren. Otherwise the stack is syntactically correct.

## 4
### Describe an algorithm for reversing a list using a stack.
See stack.py \
Pop each element of a stack, and add it to a new stack. Since elements are removed in reverse order, the new stack is reversed.