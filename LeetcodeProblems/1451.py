# this was someones on site interview question
# beats 60% in time and 52% in space

class Solution:
    def arrangeWords(self, text: str) -> str:
        temp = text.split()
        temp[0] = temp[0].lower()
        sl = sorted(temp, key=lambda x: len(x))
        sl[0] = sl[0].title()
        sl = " ".join(sl)
        return sl