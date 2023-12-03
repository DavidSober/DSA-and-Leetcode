# beats 78% in time and 83% in space

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        tot = len(arr)
        ans = removed = 0
        F = Counter(arr)
        temp = sorted(F.values())
        while temp:
            removed += temp.pop()
            ans += 1
            if removed >= tot // 2:
                break
        return ans