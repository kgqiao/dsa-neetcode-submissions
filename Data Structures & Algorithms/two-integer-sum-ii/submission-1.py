class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #Given:
        #numbers = [] #Given array of integers in ascending order
        #target = 0 #Given integer number

        if numbers is None or target is None: #If numbers input doesn't exist, break function
            return [-1, -1] #Return non answer to adjere with required return argument

        i, j = 0, len(numbers)-1  #Initialize two pointers left and right ends

        while i != j and i < j: #while i & j don't corss and i & j don't pass each other
            sum = numbers[i] + numbers[j] #Sum up elements of those current indexes' elements
            if sum == target: #yes found pair
                return [i + 1, j + 1] #Required (1-indexed) --> so move up indices by 1
            elif sum < target: #too small, increase i left pointer
                i += 1
            elif sum > target: #too large, dec j right pointer
                j -= 1
            
        #else if got to this point, no answer
        return [-1, -1] #no solution

object1 = Solution()

#Given
numbers = [1,2,3,4]
target = 3

#Test cases
result = object1.twoSum(numbers, target)
