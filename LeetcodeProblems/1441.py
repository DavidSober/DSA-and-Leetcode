class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        stack = []
        ans = []
        pos = 0
        for i in range(1, n + 1):
            if stack == target:
                break
            if i == target[pos]:
                ans.append('Push')
                stack.append(i)
                pos += 1
            elif i != target[pos]:
                ans.append('Push')
                ans.append('Pop')
        return ans