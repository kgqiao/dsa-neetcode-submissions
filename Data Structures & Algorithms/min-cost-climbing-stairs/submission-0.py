class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        opt = [0]*(n+1)

        #name base cases:
        opt[0] = 0 #able to step on 0th floor for free
        opt[1] = 0 #able to step on 0th floor for free

        for i in range(2, n+1): #if n >= 2
            #cost to get to this i step + pay now this ith step
            opt[i] = min(opt[i-1] + cost[i-1], opt[i-2] + cost[i-2])
        
        return opt[n]

