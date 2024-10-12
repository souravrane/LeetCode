class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        remainingGas = 0
        start = 0
        fuel = 0

        for i in range(len(gas)):
            remainingGas += gas[i] - cost[i]
            fuel += gas[i] - cost[i]
            if fuel < 0:
                start = i + 1
                fuel = 0
        
        if remainingGas >= 0: return start
        return -1
            
            
        