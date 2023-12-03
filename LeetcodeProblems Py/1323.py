# you can use the replace method but its cheese for an interview
# beats 97% in time and 64% in space

class Solution:
    def maximum69Number (self, num: int) -> int:
        ans = num
        lst = [c for c in str(num)]
        for i in range(len(lst)):
            temp = lst.copy()
            if temp[i] == '6':
                temp[i] = '9'
                ans = max(ans, int("".join(temp)), num)
                break
        return ans