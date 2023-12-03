# binary exponentiation. How would one come up with this in an interview?
# log n time and log n space
# beats 85% in time and 40% in space

class Solution:
    def myPow(self, x: float, n: int) -> float:
        def binexp(x, n):
            if n == 0:
                return 1
            elif n < 0:
                return 1 / binexp(x, -n)
            if n % 2 == 0:
                return binexp(x*x, n / 2)
            else:
                return x * binexp(x*x, (n - 1) / 2)
        return binexp(x, n)
    
# here was my first approach which is brute force + memoization
# it works for 99% of cases and fails because of stack overflow
# there is no way to do tail recursion in python so this is as optimized as this
# solution can get... yes I can actually blame the language and its legit
# the only way to improve this in python is to take the binary exponentiation approach
# stack overflow beats 99% of test cases

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        cache = {}
        if n > 0:
            def rec(x, n):
                if n == 1:
                    return x
                if n in cache:
                    return cache[n]
                else:
                    result = x * rec(x, n - 1)             
                cache[n] = result
                return result
            return rec(x, n)
        else:
            def rec(x, n):
                if n == -1:
                    return 1/x
                if n in cache:
                    return cache[n]
                else:
                    result = (1/x) * rec(x, n + 1)
                cache[n] = result
                return result 
            return rec(x, n)