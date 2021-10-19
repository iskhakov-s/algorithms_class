## 1
```
T(0) = 0
T(1) = 1
T(n) = -4*T(n - 1) - 4*T(n - 2)

t^n = -4t^(n-1) -4t^(n-2)
t^n + 4t^(n-1) + 4t^(n-2) = 0
t^(n-2) (t^2 + 4t + 4) = 0
t = -2

T(n) = (a+bn)(-2)^n
a = 0
1 = (a+b)(-2)
1 = -2a - 2b
b = -1/2
T(n) = (-1/2n)(-2)^n
```

## 2
```
T(0) = 2
T(1) = 1
T(n) = T(n - 1) + 2*T(n - 2) + 2

t^n = t^(n-1) + 2t^(n-2)
t^n - t^(n-1) - 2t^(n-2) = 0
t^(n-2) (t^2 - t - 2) = 0
t= -1, 2

c = c + 2c + 2
c = -1

T(n) = a(-1)^n + b(2)^n - 1
2 = a + b - 1
3 = a + b
1 = -a + 2b - 1
2 = -a + 2b
5 = 3b
b = 5/3
a = 4/3
T(n) = (4/3)(-1)^n + (5/3)(2)^n - 1
```

## 3 - Incorrect
```
T(0) = 3
T(1) = 5
T(n) = 4*T(n - 1) - 3*T(n - 2) + n

t^n = 4t^(n-1) - 3t^(n-2)
t^n - 4t^(n-1) + 3t^(n-2) = 0
t^(n-2) (t^2 - 4t + 3) = 0
t = 1, 3

cn = 4c(n-1) - 3c(n-2) + n
cn = 4cn - 4c - 3cn + 6c + n
0 = 2c + n

cn = 4c(n - 1) - 3c(n - 2) + n
cn - 4c(n - 1) + 3c(n - 2) = n
c(n - 4(n-1) + 3(n-2)) = n
c = n / (n - (4n-4) + (3n-6))
c = -n/2
d = 4d - 3d + n
d = n
cn+d = n(-n/2)+n # it should be n(-n/4)+n

T(n) = a + b(3)^n + n(1-n/2)
3 = a + b
5 = a + 3b + 1/2
9/2 = a + 3b
3/2 = 2b
b = 3/4
a = 9/4
T(n) = (9/4) + (3/4)(3)^n + n(1-n/2)
# should be T(n) = 1/8 (-2 n (n + 4) + 13 3^n + 11)
```

## 4
```
T(0) = 9
T(1) = 10
T(2) = 32
T(n) = 7*T(n - 2) + 6*T(n - 3)

t^n = 7t^(n-2) + 6t^(n-3)
t^n - 7t^(n-2) - 6t^(n-3) = 0
t^(n-3) (t^3 - 7t - 6) = 0
t = -2, -1, 3

T(n) = a(-2)^n + b(-1)^n + c(3)^n
9 = a + b + c
10 = -2a - b + 3c
32 = 4a + b + 9c
# Solve using rref
a = -3
b = 8
c = 4
T(n) = -3(-2)^n + 8(-1)^n + 4(3)^n
```