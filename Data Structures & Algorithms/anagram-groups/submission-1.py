class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #Given:
        #strs = [] #array of strings - 1 level
        anagrams_dict = {} #initialize empty dict

        for i, word in enumerate(strs): #Sort each word (array's string items)
            sorted_word = "".join(sorted(word)) #Store stored version of word value
            #Evaluate sorted word now in anagrams_dict, see if exists
            if sorted_word in anagrams_dict: #yes, sorted_word exists as a key in anagrams_dict
                anagrams_dict[sorted_word].append(word) #add array item to value of dict's that key: my_dict[desired_key] = (newitem_of_array_val)
            else: #Not in anagrams_dict currently, add as new key and value (aka array w single word value)
                anagrams_dict[sorted_word] = [word] #Add new key: [word]
        
        #Convert to a nested list of values
        nested_array = [val_words for val_words in anagrams_dict.values()]
        return nested_array


#Object declaration of class instance
object1 = Solution()

#Given
strs1 = ["act","pots","tops","cat","stop","hat"]
strs2 = ["x"]

#Test cases
object1.groupAnagrams(strs1) #Expected Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
object1.groupAnagrams(strs2) #Expected Output: [["x"]]





# NOTES for later: Convert to a nested list of [key, value] pairs: nested_array = [[key_sorted_word, val_words] for key_sorted_word, val_words in anagrams_dict.items()]