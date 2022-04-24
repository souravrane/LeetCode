class Event:
    def __init__(self, id, stationName, t):
        self.id  = id
        self.stationName = stationName
        self.t = t

        
class Average:
    def __init__(self):
        self.totalTime = 0
        self.count = 0
    
    def updateAvg(self, timeDiff):
        self.totalTime += timeDiff
        self.count += 1
    
    def getAvg(self):
        return self.totalTime / self.count
    
    
class UndergroundSystem:

    def __init__(self):
        self.eventReg = {}
        self.averages = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        if id in self.eventReg: return
        self.eventReg[id] = Event(id, stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        if id not in self.eventReg: return
        name = self.eventReg[id].stationName + ',' + stationName
        
        if name not in self.averages:
            self.averages[name] = Average()
        
        self.averages[name].updateAvg(t - self.eventReg[id].t)
        del self.eventReg[id]


    def getAverageTime(self, startStation: str, endStation: str) -> float:
        name = startStation + "," + endStation
        return self.averages[name].getAvg()


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)