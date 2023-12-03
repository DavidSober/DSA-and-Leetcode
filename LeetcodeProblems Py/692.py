# beats 54% in time and 45% in space
# this problem was ez but i kept getting an error due to how the sorted function works
# essentially if you have a tuple of criteria for which you are sorting in a lambda function, you should not use 
# the reverse=True arg. this is because in our tuple we have a sorting heirarchy and using reverse=True
# will reverse that entire heirarchy.
# i did sorted(F.keys(), key=lambda x: (F[x], x), reverse=True)[:k] 
# what this did was sorted first by frequency (which is right) then by lexi order (good so far) and then we 
# reverse. so now we sort by descending freq (good still) and reverse lexi order (this is where it breaks)

# it breaks bc we want normal lexi order (not reverse) and we want descending freq at the same time
# reverse=True breaks this badly 

# lesson here is if you use a tuple for sorting criteria, do not use reverse at all if possible. it can mess things 
# up un unpredictable ways. instead use a negative if you need to such as -F[x]

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        F = Counter(words)
        ret = sorted(F.keys(), key=lambda x: (-F[x], x))[:k]
        return ret