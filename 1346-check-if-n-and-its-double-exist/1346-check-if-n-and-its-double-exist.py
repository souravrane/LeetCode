class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        hashSet = set()
        for num in arr:
            if num*2 in hashSet or num / 2 in hashSet: return True
            hashSet.add(num)
        return False