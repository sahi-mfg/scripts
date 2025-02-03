"""
We will write the fibonacci sequence using a generator using multiple paradigms
and see how they compare in terms of performance and space and time complexity.

I was inspired by this article on medium:

"My Interviewer Asked Me About Fibonacci, but He Didn’t Like My Answer" By: Lory
 
"""
from functools import lru_cache

def recursive_fibonacci(n):
    if n <= 1:
        return n
    return recursive_fibonacci(n-1) + recursive_fibonacci(n-2)


def iterative_fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def iterative_fibonacci2(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    prev, curr = 0, 1
    for _ in range(2, n+1):
        prev, curr = curr, prev + curr
    return curr

def fibonacci_tco(n, a=0, b=1):
    if n == 0:
        return a
    if n == 1:
        return b
    return fibonacci_tco(n-1, b, a+b)


@lru_cache(maxsize=None)
def fibonacci_memoization(n):
    if n <= 1:
        return n
    return fibonacci_memoization(n-1) + fibonacci_memoization(n-2)


def fibonacci_dp(n):
    if n <= 1:
        return n
    dp = [0] * (n+1)
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

def fibonacci_matrix(n):
    pass

def fibonacci_binet(n):
    pass


def main() -> None:
    n = 10
    print(recursive_fibonacci(n))
    print(iterative_fibonacci(n))
    print(iterative_fibonacci2(n))

if __name__ == "__main__":
    main()

