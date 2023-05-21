# 27% in time and 20% in space

class Solution:
    def capitalizeTitle(self, title: str) -> str:
        new = title.split()
        for i in range(len(new)):
            if len(new[i]) < 3:
                new[i] = new[i].lower()
            else:
                new[i] = new[i].capitalize()
        ret = ""
        for word in new:
            ret += word + " "
        return ret[:len(ret) - 1]