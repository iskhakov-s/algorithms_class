## 1 - Pow10
The slow algorithm recurs with subtraction, while the fast algorithm recurs with division.
Therefore, the algorithms have complexities of `O(n)` and `O(logn)` (which is faster), respectively.

## 2
```
T(0) = 2
T(1) = 1
T(n) = T(n - 1) + 2*T(n - 2)

t^n = t^(n-1) + 2t^(n-2)
t^n - t^(n-1) - 2t^(n-2) = 0
t^(n-2) * (t^2 - t - 2) = 0
t = -1, 2

T(n) = a*(-1)^n + b*2^n
2 = a + b
1 = -a + 2b
3 = 3b
b = 1
a = 1
T(n) = (-1)^n + 2^n
```

## 3
```
T(0) = 5
T(n) = 3*T(n - 1)

t^n = 3*t^(n-1)
t^n - 3*t^(n-1) = 0
t^(n-1) * (t - 3) = 0
t = 3

T(n) = a*3^n
5 = a*1
a = 5
T(n) = 5 * 3^n
```

## 4
```
T(0) = 3
T(1) = 6
T(n) = 2*T(n - 1) + 8*T(n - 2)

t^n = 2*t^(n-1) + 8*t^(n-2)
t^n - 2*t^(n-1) - 8*t^(n-2) = 0
t^(n-2) * (t^2 - 2t - 8) = 0
t = -2, 4

T(n) = a*(-2)^n + b*4^n
3 = a + b
6 = -2a + 4b
12 = 6b
b = 2
a = 1
T(n) = 1*(-2)^n + 2*4^n
T(n) = (-2)^n + 2*4^n
```

## 5 - Fibonacci
```
T(0) = 0
T(1) = 1
T(n) = T(n - 1) + T(n - 2)

t^n = t^(n-1) + t^(n-2)
t^n - t^(n-1) - t^(n-2) = 0
t^(n-2) * (t^2 - t - 1) = 0
t = (1-sqrt5)/2, (1+sqrt5)/2
```