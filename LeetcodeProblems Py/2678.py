class Solution:
    def countSeniors(self, details: List[str]) -> int:
        return sum(1 for detail in details if int(detail[11:13]) > 60)



class Solution:
    def countSeniors(self, details: List[str]) -> int:
        ans = 0
        temp = []
        for detail in details:
            if int(detail[11:13]) > 60:
                ans += 1
                temp.append(detail[11:13])
        print(temp)
        return ans