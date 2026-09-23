class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums is None:
            return -1
        elif nums is []:
            return -1

        l, r = 0, len(nums)-1

        while l <= r: #while binary window has not closed
            mid = l + (r-l)//2 #find midpoint index
            if target == nums[mid]: #found
                return mid
            elif target < nums[mid]:
                r = mid-1
            elif target > nums[mid]:
                l = mid+1
            
        return -1
        