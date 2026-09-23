class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        opt = [0] * (n)

        if n == 0:
            return 0
        elif n == 1:
            return nums[0]
        
        opt[0] = nums[0] #First house
        opt[1] = max(opt[0], nums[1]) #2nd house

        for i in range(2, n):
            opt[i] = max(nums[i] + opt[i-2], opt[i-1])

        return opt[n-1]
