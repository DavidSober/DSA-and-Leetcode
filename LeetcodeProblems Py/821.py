# beats 8% in time and 11% in space
class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        ans = []
        idx = defaultdict(list)
        for i in range(len(s)):
            if s[i] == c:
                idx[c].append(i) # first get the all indexes for c
        for i in range(len(s)):
            minn = float('inf')
            for j in idx[c]:        
                delta = abs(i - j)      # then we calc the distance between curr index i and indexes j 
                minn = min(minn, delta) # we find the min abs difference between curr index i and index of c aka index j
            ans.append(minn) # append smallest index to ans then return it 
        return ans