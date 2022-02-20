class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:

        pf = [0]*n
        for flight in bookings:
            first,last,seats = flight
            pf[first-1] += seats
            if last < n:
                pf[last] -= seats
            
        for i in range(1,n):
            pf[i] += pf[i-1]
        
        return pf