class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #Given 
        #nums = [] #array of integer values
        #k = # # A desired number of most frequent elements

        freq_ht = {} #Initialize empty dict

        for i, element in enumerate(nums):
            if element in freq_ht: #if element already exists in ht as a key
                freq_ht[element] = freq_ht[element] + 1 #inc value of ht's key at that element += 1
            else: #Element not seen in ht yet, add as new key
                freq_ht[element] = 1
        
        freq_ht = dict(sorted(freq_ht.items(), key = lambda items: items[1], reverse = True)) #once viewed all elements, sort dict
        freq_arr = list(freq_ht) #Convert dict to array
        
        return freq_arr[0:k]


object1 = Solution()

#Given:
nums1 = [1,2,2,3,3,3]
k1 = 2
nums2 = [7,7]
k2 = 1

object1.topKFrequent(nums1, k1) #Expected Output: [2,3]
object1.topKFrequent(nums2, k2) #Expected Output: [7]