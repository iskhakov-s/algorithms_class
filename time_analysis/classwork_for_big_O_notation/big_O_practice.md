Big-O notation classifies algorithms by how much the runtime and memory requirements correlate with the input size.
For big-O notation, only the most complex component matters, and coefficients are discarded.

Ordering for big-O complexity (k is any constant):
 1. *O(1)* least complex
 2. *O(logn)*
 3. *O(n)*
 4. *O(n<sup>k</sup>)* more complex with greater k (k>1)
 5. *O(k<sup>n</sup>)* more complex with greater k (k>1)
 6. *O(n!)*
 7. *O(n<sup>n</sup>)* most complex

 ---

 ### 1
 *f(n) = 10n<sup>8</sup> + log<sub>3</sub>(n<sup>2</sup> + n) + √(2<sup>n-2</sup>)*

 *O(f(n)) = O(√2<sup>n</sup>)*
 
*√(2<sup>n-2</sup>)* simplifies to *(√2)<sup>n</sup>* by rearranging and removing constants. 
Exponential is more complex than polynomial, so term 1 can be ignored.
*logn<sup>2</sup>* is less complex because *logn* is less complex than the constant,
 and *n<sup>2</sup>* is less complex than the exponential, so term 2 can be ignored.

 ### 2
 *logn* is less complex than *n* so if they are added only *n* remains.

 ### 3
 All logarithms of different bases are related by constant factors, so the base doesn't matter.

 ![](log_division.png)

### 4
See *bottles_of_beer.py*

### 5
For a given input n, the song calls for two printed lines from 0-n, which is 2n+2 lines.