# beats 78% in time and 28% in space
'''Explanation
cur means the current decoded element.

For each element we have
A[i] = res[i] ^ res[i+1]
A[i] ^ A[i] ^ res[i+1] = res[i] ^ res[i+1] ^ A[i] ^ res[i+1]
res[i+1] = res[i] ^ A[i]'''

class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        ans = [first]
        for i in range(len(encoded)):
            ans.append(encoded[i] ^ ans[-1])
        return ans