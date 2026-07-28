class Solution: #Latest self solution O(N log N) - 07/28/2026
    def longestConsecutive(self, nums: List[int]) -> int:
        #Given
        #nums = [] #Given array of integers

        if not nums: 
            return 0

        nums = sorted(list(set(nums))) # Sort and remove duplicates (handles cases like nums2)

        longest_streak = 1 #initialize for empty manipulation
        current_streak = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] + 1: #if curr nums is consecutive to prev element at nums[i-1]
                current_streak += 1 #increase current_streak by 1
            else: #if not consecutive, goes until streak breaks, and we see how far we got with current streak
                longest_streak = max(longest_streak, current_streak) #reupdate what's the longest streak so far
                current_streak = 1 #reset counter of the "streak we're currently looking at"

        return max(longest_streak, current_streak)

object1 = Solution()

#Given
nums1 = [2,20,4,10,3,4,5]
nums2 = [0,3,2,5,4,6,1,1]

#test cases
result1 = object1.longestConsecutive(nums1) #Expected Output: 4
result2 = object1.longestConsecutive(nums2) #Expected Output: 7