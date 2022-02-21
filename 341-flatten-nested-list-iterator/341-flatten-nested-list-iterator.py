# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.curr = 0
        self.flattenList = []
        for element in nestedList:
            self.extract(element)
            
    
    def next(self) -> int:
        self.curr += 1
        return self.flattenList[self.curr - 1]
           
        
    def hasNext(self) -> bool:
        return self.curr < len(self.flattenList)
        
    
    def extract(self,value):
        if value.isInteger():
            self.flattenList.append(value.getInteger())
        else:
            for element in value.getList():
                self.extract(element)
        
# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())