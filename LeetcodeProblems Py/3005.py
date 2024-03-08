class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        F = Counter(nums)
        mxlst = sorted(F.keys(), key = lambda x: -F[x])
        mx = F[mxlst[0]]
        mxnums = []
        for num in mxlst:
            if F[num] == mx:
                mxnums.append(num)
            else:
                break
        return len(mxnums) * mx