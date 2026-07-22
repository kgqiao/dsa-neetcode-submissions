class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]: #Min Heap Solution
        count = {} #Create empty dict
        for num in nums: #Loop through nums integer array
            count[num] = 1 + count.get(num, 0) #Increment count of existing value in dict where seen

        heap = [] #initialize heap
        for num in count.keys(): #for each num_key in count_dict's keys:
            heapq.heappush(heap, (count[num], num)) #heappush() heap by count of counts, aka add to heap in order of highest frequency
            if len(heap) > k: #if len of heap ever exceeds k, 
                heapq.heappop(heap) #pop out the element with the lowest freq counter

        res = []
        for i in range(k): #Create list out last k elements (from largest to smallest)
            res.append(heapq.heappop(heap)[1])
        return res
        