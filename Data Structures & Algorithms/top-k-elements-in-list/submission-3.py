class Solution: #Attempt #3 08/20/2026
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if nums is None:
            return []

        freq_ht = {}
        for i in range(len(nums)):
            if nums[i] in freq_ht:
                freq_ht[nums[i]] = freq_ht[nums[i]] + 1
            else: 
                freq_ht[nums[i]] = 1
        
        freq = dict(sorted(freq_ht.items(), key = lambda item: item[1], reverse = True))
        arr = list(freq)
        return arr[0:k]