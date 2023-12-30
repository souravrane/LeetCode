class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senateQ = deque(senate)
        tempQ = deque()
        while True:
            senator = senateQ.popleft()
            print(senator)
            while senateQ and senator == senateQ[0]:
                tempQ.append(senateQ.popleft())
   
            if senateQ:
                senateQ.popleft() # evict the opponent
                senateQ.append(senator)
                senateQ.extendleft(tempQ)
                tempQ.clear()
            else:
                return "Radiant" if senator == 'R' else "Dire"
            

        
        