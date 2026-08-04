class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #given
        #piles =[]
        #h = 0

        low, high = 1, max(piles)
        resulting_k = high
        
        while low <= high: #look for possible size of k
            k = low + (high-low)//2
            if k == 0: 
                low = 1
                continue

            g = 0
            #HOW many multiples of k does it take to eat all bananas across all piles
            for p in piles:
                g += math.ceil(p / k) #O(1) search of how many rounds of k it takes to eat up all bananas in element
                
            #hypothetically, did g hours go under h hours?
            if g <= h: #if all bananas were finished within h hours
                resulting_k = k #Most recently minimum found k
                high = k - 1 #see if can increase k higher
            else: #not all bananas were eaten
                low = k + 1

        return resulting_k