class Solution:
    def isPalindrome(self, s: str) -> bool:
        #Given
        # s = "" #String given
        s = s.lower() #Convert string all to lowercase

        if not s:
            return False #If not s valid input, return None

        i, j = 0, len(s)-1 #Initialize the two pointerse

        while i != j and i < j: #While the two pointers have not crossed, and i is still to the left of j
            if not s[i].isalnum(): #if either i or j position is a non alphanumeric char, skip
                i += 1
                continue

            if not s[j].isalnum(): #if either i or j position is a non alphanumeric char, skip
                j -= 1
                continue

            if s[i] == s[j]: #If letters equal
                i += 1 #Shift pointers
                j -= 1
            else: #not equal
                return False
        
        #If made it to here, must be palindrome
        return True


object1 = Solution()

#Given
s1 = "Was it a car or a cat I saw?"
s2 = "tab a cat"

#Test cases
result1 = object1.isPalindrome(s1) #Expected Output: True
result2 = object1.isPalindrome(s2) #Expected Output: False