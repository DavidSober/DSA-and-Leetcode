# beats 91% in time and 42% in space

class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:

        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        prefix = [days[0]]
        for i in range(1, len(days)):
            prefix.append(prefix[-1] + days[i - 1])
        print(prefix)

        Asd = arriveAlice.split('-') # Asd = alice start date
        for i in range(len(Asd)):
            Asd[i] = int(Asd[i])

        Aed = leaveAlice.split('-')
        for i in range(len(Aed)):
            Aed[i] = int(Aed[i])

        AedMonth = prefix[Aed[0] - 1] # end month
        AsdMonth = prefix[Asd[0] - 1] # start month

        alicedays = list(range(AsdMonth + Asd[1] , AedMonth + Aed[1] + 1))

        print(alicedays, len(alicedays))

        Bsd = arriveBob.split('-') # Asd = alice start date
        for i in range(len(Bsd)):
            Bsd[i] = int(Bsd[i])

        Bed = leaveBob.split('-')
        for i in range(len(Bed)):
            Bed[i] = int(Bed[i])

        BedMonth = prefix[Bed[0] - 1] # end month
        BsdMonth = prefix[Bsd[0] - 1] # start month

        bobdays = list(range(BsdMonth + Bsd[1], BedMonth + Bed[1] + 1))
        print(bobdays, len(bobdays))

        # match the days list
        ans = 0
        overlap = Counter(alicedays) + Counter(bobdays)
        for key in overlap:
            if overlap[key] == 2:
                ans += 1
        return ans