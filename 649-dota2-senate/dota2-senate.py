class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        radiant = deque()
        dire = deque()
        for index, party in enumerate(senate):
            if party == 'R': radiant.append(index)
            else: dire.append(index)
        
        n = len(senate)
        while radiant and dire:
            firstR = radiant.popleft()
            firstD = dire.popleft()
            
            if firstR < firstD:
                radiant.append(firstR + n)
            else:
                dire.append(firstD + n)
            
        return "Radiant" if radiant else "Dire"

        
        