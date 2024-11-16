import math
import os
import functools


@functools.lru_cache(maxsize=None)  # Memoization decorator
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

def find_pair(lst):
    
def find_pair_with_sum(lst, target_sum):
    seen = set()
    for num in lst:
        complement = target_sum - num
        if complement in seen:
            return (complement, num)
        seen.add(num)
    return None

        for j in range(i+1, len(lst)):
            if lst[i] + lst[j] == 10:
                return (lst[i], lst[j])
    return None