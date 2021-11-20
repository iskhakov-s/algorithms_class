## 1
### Determine the order of the numbers that are popped.
See testing.py \
3,1,2

## 2
### Without changing the order of the push operations, insert pop operations at the right places so that the order of the numbers that are popped is 5, 2, 3, 1, 4, 6.
See testing.py

## 3
### The numbers 6, 5, 4, 3, 2, and 1 are pushed on to a stack, in that order. Give an example of a sequence of output popped numbers that is impossible, when only inserting pop operations is allowed. Explain why your sequence is impossible.
1,3,2,4,5,6 \
If 1 is the first number to be removed, then the stack is already filled with all the numbers, and the next number on top would be 2, so any other number could not be popped.

## 4
### Describe an algorithm for computing the value of a postfix expression, using a stack.
Iterate through the input. If it is a number, push it to the stack. If it is an operation, pop twice and apply the operation to the two numbers. The result is pushed to the stack. If the expression given is appropriate, then there should only be one value left in the stack, which is returned.