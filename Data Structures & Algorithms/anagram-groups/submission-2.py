class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #anagrams become identical when sorted
        seen_ht = {}
        for i, word in enumerate(strs): #loop through each word in array of strings
            sorted_word = "".join(sorted(word)) #sort current word (which goes into per char array), then joins char back together into string
            if sorted_word in seen_ht: #if sorted_word exists among the keys
                seen_ht[sorted_word].append(word) #Add new value to existing key (sorted_word)
            else: #not seen in key
                seen_ht[sorted_word] = [word] #Add new key and word value

        seen_list = list(seen_ht.values()) #convert ht's values into a list(array)
        return seen_list
    
