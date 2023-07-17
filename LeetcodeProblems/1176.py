# beats 30% in time and 85% in space

class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        tot = ans = 0
        for i in range(k):
            tot += calories[i]
        left = 0
        right = k - 1
        while right < len(calories) - 1:
            if tot < lower:
                ans -= 1
            elif tot > upper:
                ans += 1
            tot -= calories[left]
            left += 1
            right += 1    
            tot += calories[right]
        
        if tot < lower:
            ans -= 1
        elif tot > upper:
            ans += 1
            
        return ans