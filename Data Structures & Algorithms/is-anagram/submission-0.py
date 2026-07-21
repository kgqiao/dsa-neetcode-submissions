class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Given
        # s = string #1
        # t = string #2
    
        arr_s = list(s) #Convert string #1 into an array

        for char in t: #Loop through each character in t
            if char in arr_s: #if current char of t exists in arr_s
                arr_s.remove(char) #Remove character from arr_s
            else: #Current characgter of t doesn't exist in arr_s: ok, then not anagram
                return False
        
        #If got to finish for loop, then all letters of t matched a letter in s
        #check if s had any remaining letters that t didn't have
        if len(arr_s) != 0: #aka not all letters of s were cleared
            return False
        else:
            return True


object1 = Solution()

s = "racecar"
t = "carrace"

s2 = "jar"
t2 = "jam"

result1 = object1.isAnagram(s, t) #Expected Output: True
result2 = object1.isAnagram(s2, t2) #Expected Output: False