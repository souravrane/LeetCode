class MyCalendar:
    '''
    [4,10]  [9,15] -> merge
    
    [4,10]  [1,9]
    
    [4,10]  [1,4] -> no merge , 10 > 1 and 
    
    '''
    '''
            
    [10,20]  
    [35,40] [20,35]
    '''

    def __init__(self):
        self.calendar = []
    
    def checkMerge(self, newStart, newEnd):
        for i in range(len(self.calendar)):
            currStart, currEnd = self.calendar[i]
            
            if currStart >= newEnd:
                self.calendar.insert(i,[newStart, newEnd])
                return True
            elif currEnd > newStart and currStart < newEnd:
                return False
        
        self.calendar.append([newStart,newEnd])
        return True
            
            
                
                 
            
            
        return True
    
    def book(self, start: int, end: int) -> bool:
        if len(self.calendar) == 0:
            self.calendar.append([start,end])
            return True
        
        return self.checkMerge(start,end)
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)