class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        
        def is_prime(n):
            if n <= 1:
                return False
            elif n <= 3:
                return True
            elif n % 2 == 0 or n % 3 == 0:
                return False
            i = 5
            while i * i <= n:
                if n % i == 0 or n % (i + 2) == 0:
                    return False
                i += 6
            return True
    
        d1 = [nums[i][i] for i in range(len(nums))]
        d2 = [nums[i][len(nums)-i-1] for i in range(len(nums))]
        d1prime = []
        d2prime = []
        for num in d1:
            if is_prime(num):
                d1prime.append(num)
        for num in d2:
            if is_prime(num):
                d2prime.append(num)
        total = d1prime + d2prime
        if len(total) == 0:
            return 0
        else:
            return max(total)