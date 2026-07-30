class Solution: #07/30 Could not solve, reviewed solution
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1 #Initialize left and right pointers on opposite ends of the array
        res = 0 #Initialize "area" calculation as zero

        while l < r: #While the two pointers have not crossed
            area = min(heights[l], heights[r]) * (r - l) #Calculate area = smaller of two heights x width between pointers
            res = max(res, area) #Find the larger of the two areas (currently vs most recently largest area calculated)
            if heights[l] <= heights[r]: #Move the pointer with the shorter height
                l += 1 #if l pointer has the shorter height, move it right --> 
            else:
                r -= 1 #if r pointer has the shorter height, move it left <---
        return res #Do until l and r has crossed, and at that point the res = the most recently viewed largest area calculation