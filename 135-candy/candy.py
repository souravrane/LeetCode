class Solution:
    def candy(self, rating: List[int]) -> int:
        candies = [1]*len(rating)
        for i in range(1,len(candies)):
            if rating[i-1] < rating[i]:
                candies[i] = candies[i-1] + 1
            
        for i in range(len(candies)-2, -1, -1):
            if rating[i] > rating[i+1]:
                candies[i] = max(candies[i], candies[i+1] + 1)
            
        return sum(candies)