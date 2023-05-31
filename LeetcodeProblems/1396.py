# beats 5.5% in time and 6% in space

class UndergroundSystem:

    def __init__(self):
        self.stor = defaultdict(list)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.stor[id].append( (stationName, t) )

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        self.stor[id].append( (stationName, t) )

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        delta = []
        for key in self.stor:
            for i in range(0, len(self.stor[key]) - 1, 2): # going through list step = 2
                if self.stor[key][i][0] == startStation and self.stor[key][i + 1][0] == endStation:
                    delta.append(abs(self.stor[key][i][1] - self.stor[key][i + 1][1]))
        return sum(delta) / len(delta)



# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)