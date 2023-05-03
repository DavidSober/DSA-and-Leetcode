# beats 5% in time and 5% in space

class Solution:
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
        if target not in words:
            return -1
        startI_copy = startIndex # save copy since we will change startI val first
        count = 0
        n = len(words)
        forward = 0
        while count < n:
            if words[startIndex % n]  != target:
                startIndex += 1
                count += 1
            else:
                forward = count
                break
        backward = 0
        count = 0
        while count < n:
            if words[startI_copy % n] != target:
                startI_copy -= 1
                count += 1
            else:
                backward = count
                break
        # print(forward, backward)
        if forward < backward:
            return forward
        else:
            return backward
            