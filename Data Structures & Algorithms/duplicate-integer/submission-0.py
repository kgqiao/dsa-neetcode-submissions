class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #Given
        #nums = [] #array being evaluated

        seen_set = set() #initialize an empty dict #BEFORE LOOP STARTS, TO KEEP HISTORY OF SEEN BEFORE VALS

        for i, val in enumerate(nums): #range covers 0 to 1 less than length of array
            if val in seen_set: #HOWTO: Check if a key exists in a dict 
                #if yes, seen before --> return True. Function completes
                return True
            else: #if no, not seen before, return false. keep searching
                seen_set.add(val) #Add new element to dict
        
        #if for loop finishes, no elemment was seen that was already in dict (aka every element was new/unique)
        return False

object1 = Solution()

nums1 = [1, 2, 3, 3]
nums2 = [1, 2, 3, 4]

object1.hasDuplicate(nums1) #Expected Output: True
object1.hasDuplicate(nums2) #Expected Output: False