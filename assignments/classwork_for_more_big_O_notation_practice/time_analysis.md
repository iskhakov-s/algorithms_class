See reference.py for the code.

### 1 - Factorial
*O(n)*:
The factorial function iterates from 2 to the number,
which is linearly related to the size of the input


### 2 - Trials
*O(1)*:
The function iterates a number of irrespective of the size of the input,
which is a constant number of operations
(Internally used functions, like randrange, that use the input may have non-constant time complexities, though)

### 3 - Draw Square
*O(n<sup>2</sup>)*:
The function iterates once through the input, then inside the iteration iterates once again.

### 4 - Add To
*O(n<sup>2</sup>)*:
The function iterates through the input, and at each step, it iterates again up to the current iterator's value.
This means that it iterates *1+2+...+n* times, which is equal to $\frac{n(n+1)}{2}$

### 5 - Middle
*O(logn)*:
The function repeatedly averages the input and a particular number until the input reaches the number.
The function repeatedly halves the distance between the numbers,
which is effectively finding 2 to the what value equals the difference, which is log.

### 6 - GCF
*O(logn)*:
The function reduces the distance between itself and 0 through division; which, as shown in #5, is log complexity.