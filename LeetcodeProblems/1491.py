# beats 43% in time and still 7% in space? any way to make it take less space?

class Solution:
    # beats 7% in time and 7% in space try harder
    # def average(self, salary: List[int]) -> float:

    #     salary.sort()
    #     salary.pop(-1)
    #     salary.pop(0)
    #     return sum(salary) / len(salary)

    ans = 0
    minn = float('inf')
    maxx = float('-inf')
    for i in range(len(salary)):
        if salary[i] > maxx:
            maxx = salary[i]
        if salary[i] < minn:
            minn = salary[i]
        ans += salary[i]
    return (ans - maxx - minn) / (len(salary) - 2)