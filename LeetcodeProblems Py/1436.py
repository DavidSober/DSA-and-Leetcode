# beats 48% in time and 9% in space

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        left = set()
        right = set()
        for pair in paths:
            left.add(pair[0])
            right.add(pair[1])
        ret = left ^ right
        for i in ret:
            if i not in left:
                return i