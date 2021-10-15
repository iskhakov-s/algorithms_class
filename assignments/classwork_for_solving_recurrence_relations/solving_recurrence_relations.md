Keep in mind that recursion stops at 1, so the largest value of n would be 2 in the non recursive part.

## 1 - Print Tri
Each time, it loops up to the number, then recurses minus 1.
This can be represented as:
```
T(n) = n + T(n-1)
T(n) = n + (n-1) + T(n-2)
T(n) = (n+(n-1)+(n-2)+...+2) + T(1)
T(n) = n(n+1)/2 - 1 + 1
T(n) = n(n+1)/2
```

## 2
```
T(n) = 1 + T(n - 1)
T(n) = 1 + 1 + T(n - 2)
T(n) = n-1 + T(1)
T(n) = n
```

## 3
```
T(n) = 2^n + T(n - 1)
T(n) = 2^n + 2^(n-1) + T(n - 2)
T(n) = 2^n + 2^(n-1) + ... + 2^3 + 2^2 + T(1)
T(n) = (2^(n+1) - 1) - 2 - 1 + T(1)
T(n) = 2^(n+1) - 3
```

## 4
Approximately equal since integer division would be used

This uses the rule that repeated division means log with the divisor as the base
```
T(n) = 1 + T(n/2)
T(n) = 1 + 1 + T(n/4)
T(n) = log2(n) + T(1)
T(n) = log2(n) + 1
```

## 5
Approximately equal since integer division would be used

This uses the sum of a geometric sequence equation
```
T(n) = n + T(n/2)
T(n) = n + n/2 + T(n/4)
T(n) = n(1-0.5^log2(n))/(1-0.5) +T(1)
T(n) = 2n(1-0.5^log2(n)) + 1
```

## 6 - Mystery Sum
This uses the sum of first n squares equation

The number is iterated in 2 nested for loops, the recurses minus 1.
This can be represented as:
```
T(n) = n^2 + T(n-1)
T(n) = n^2 + (n-1)^2 + T(n-2)
T(n) = n^2 + (n-1)^2 + ... + 3^2 + 2^2 + T(n)
T(n) = n(n+1)(2n+1)/6 - 1 + 1
T(n) = n(n+1)(2n+1)/6
```

## 7
```
T(n) = 1 + 2*T(n - 1)
T(n) = 1 + 2*(1 + 2*T(n - 2))
T(n) = 1 + 2 + 4*T(n - 2)
T(n) = 1 + 2 + 4*(1+2*T(n - 3))
T(n) = 1 + 2 + 4 + 8*T(n - 3)
T(n) = 1 + 2 + ... + 2^(n-1)
T(n) = 2^(n) - 1
```