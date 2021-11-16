## 1
```
T(1) = 1
T(n) = T(n-1) + 1
T(n) = T(n-2) + 1 + 1
T(n) = T(1) + n-1
T(n) = n
```

## 2
```
T(0) = 2
T(n) = 4*T(n - 1) + n

t^n = 4t^(n-1)
t^n - 4t^(n-1) = 0
t^(n-1) (t-4) = 0
t = 4

T(n) = a*4^n + cn + d
a*4^n + cn + d = 4(a*4^(n-1) + c(n-1) + d) + n
a*4^n + cn + d = a*4^n + 4cn - 4c + 4d + n
cn + d = 4cn - 4c + 4d + n
0 = 3cn - 4c + 3d + n
3cn + n = 0
c = -1/3
0 = -n + 4/3 + 3d + n
d = -4/9

T(n) = a*4^n  -1/3n  -4/9
2 = a - 4/9
a = 22/9
T(n) = (22/9)*4^n - 1/3n - 4/9
```

## 3
```
T(0) = 2
T(1) = 5
T(n) = 3*T(n - 1) + 10*T(n - 2)

t^n = 3t^(n-1) + 10t^(n-2)
t^n - 3t^(n-1) - 10t^(n-2) = 0
t^(n-2) = (t^2 - 3t - 10) = 0
t = -2, 5

T(n) = a(-2)^n + b(5)^n
2 = a + b
4 = 2a + 2b
5 = -2a + 5b
9 = 7b
b = 9/7
a = 5/7
T(n) = (5/7)(-2)^n + (9/7)(5)^n
```

## 4
```
T(0) = 2
T(1) = 7
T(2) = 12
T(n) = -6T(n - 1) + 12*T(n - 2) - 8*T(n - 3)

t^n = -6t^(n-1) + 12t^(n-2) - 8t^(n-3)
t^n + 6t^(n-1) - 12t^(n-2) + 8t^(n-3) = 0
t^(n-3) (t^3 + 6t^2 - 12t + 8) = 0
t = -7.69464

T(n) = a*(-7.69464)^n
2 = a
T(n) = 2*(-7.69464)^n
```
Something went wrong, only 1 root exists\
WolframAlpha couldn't compute either...\
The relation also gives negative values for odd numbers (see q4.py), which may be why it works strangely.
