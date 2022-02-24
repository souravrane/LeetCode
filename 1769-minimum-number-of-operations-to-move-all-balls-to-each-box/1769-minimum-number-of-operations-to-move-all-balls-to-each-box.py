class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        res = []
        for i in range(len(boxes)):
            s = 0
            
            for j in range(len(boxes)):
                if boxes[j] == '1':
                    s += abs(j-i)
                    
            res.append(s)
        
        return res
        