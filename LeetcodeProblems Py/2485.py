class Solution:
    def pivotInteger(self, n: int) -> int:
        if n < 2:
            return 1
        lst = [i for i in range(1, n + 1)]
        pre = [lst[0]]
        for i in range(1, n):
            pre.append(lst[i] + pre[i - 1])
        
        for i in range(len(lst)):
            if pre[i] == pre[-1] - pre[i - 1]:
                return i + 1


        return -1