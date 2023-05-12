# beats 14% in time and 21% in space
class Solution:
    def toLowerCase(self, s: str) -> str:
        new = []
        for c in s:
            new.append(c)
        for i in range(len(new)):
            if new[i].isupper():
                new[i] = new[i].lower()
        temp = "".join(new)
        return temp 