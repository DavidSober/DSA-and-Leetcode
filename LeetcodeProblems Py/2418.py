class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        mp = []
        for name, height in zip(names, heights):
            mp.append([name, height])
        
        temp =  sorted(mp, key=lambda x: -x[1])
        ans = []
        for pair in temp:
            ans.append(pair[0])
        return ans