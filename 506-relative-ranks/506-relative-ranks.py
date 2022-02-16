class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:      
        index_tracker = {}
        sorted_score = sorted(score,reverse=True)
        
        for i in range(len(sorted_score)):
            if i == 0:
                index_tracker[sorted_score[i]] = "Gold Medal"
            elif i == 1:
                index_tracker[sorted_score[i]] = "Silver Medal"
            elif i == 2:
                index_tracker[sorted_score[i]] = "Bronze Medal"
            else:               
                index_tracker[sorted_score[i]] = str(i+1)
        
        result = []
        for s in score:
            result.append(index_tracker[s])
        
        return result
            
            