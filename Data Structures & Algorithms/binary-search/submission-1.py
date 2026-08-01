class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #Given:
        #nums = []
        #target = 0

        low = 0 #Initialize high, low, and mid indices
        high = len(nums) - 1

        if not nums: #if either array or target num doesn't exist
            return -1

        while low <= high: #while binary window hasn't closed yet
            mid = low + (high - low) // 2

            if nums[mid] < target: #too small, go right, find new range by recalculating new left low end, which is above the current mid
                low = mid + 1
            elif nums[mid] > target: #too large, go left, find new range by recalculate new right/high end which is now below the current mid 
                high = mid - 1
            else: #aka target is found
                return mid
        
        #If got to this point, target was not found
        return -1