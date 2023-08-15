# beats 85% in time and 82% in space

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        F = Counter(arr)
        dist = list(filter(lambda x: F[x] == 1, arr))
        if len(dist) < k:
            return ""
        return dist[k - 1]