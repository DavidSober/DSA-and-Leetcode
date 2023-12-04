class Solution:
    def largestGoodInteger(self, num: str) -> str:
        ans = float(-inf)
        for i in range(1, len(num) - 1):
            if num[i - 1] == num[i] and num[i] == num[i + 1]:
                ans = max(ans, int(num[i - 1] + num[i] + num[i + 1])) 
        if ans == 0:
            return "000"
        elif ans == float(-inf):
            return ""
        return str(ans)