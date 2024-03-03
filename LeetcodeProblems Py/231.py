class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True
        ans = []
        def root(num):
            res = 2**(num)
            if res > n:
                ans.append(False)
                return
            elif res == n:
                ans.append(True)
                return
            
            root(num + 1)
            return
        
        root(0)
        return ans[0]