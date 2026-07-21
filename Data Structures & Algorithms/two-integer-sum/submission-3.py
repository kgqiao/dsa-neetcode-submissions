class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Given:
        #nums = [] #array of integers
        #target = 0 #integer
        
        sorted_nums = sorted(nums) #Sort array in ascending order

        i, j = 0, len(sorted_nums) - 1 #identify index positions to start for i & j

        while i != j:  #for as long as i & j don't cross i--> <--j
            sum = sorted_nums[i] + sorted_nums[j] #calculate current sum
            if sum < target: #too small, increase i left pointer by 1
                i += 1
            elif sum == target: #found pair that equals target sum, return and end
                pos1 = nums.index(sorted_nums[i]) #Find the original indices of the values that equal the target sum
                nums[pos1] = "" #replace the ith element with 0 to make sure j does not pick it up again
                pos2 = nums.index(sorted_nums[j]) 
                return [min(pos1, pos2), max(pos1, pos2)] #return the smaller of the two index numbers first, then the larger of the two index numbers second
            elif sum > target: #too large, decrease j right pointer by 1
                j -= 1
        
        #if got to this pt after loop, i & j crossed and still didn't find pair that = target_sum, must not exist
        return [-1, -1]


#Object declaration
object1 = Solution()

#Given
nums1 = [3,4,5,6]
target1 = 7
nums2 = [4,5,6]
target2 = 10
nums3 = [5,5]
target3 = 10

#Test cases
object1.twoSum(nums1, target1) #Expected Output: [0,1]
object1.twoSum(nums2, target2) #Expected Output: [0,2]
object1.twoSum(nums3, target3) #Expected Output: [0,1]
