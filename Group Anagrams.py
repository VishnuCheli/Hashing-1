#Time Complexity:: Average: TC-O(n(l*lLogl)) - extra time for converting string into a proper hashkey using a hashfunction) "U'" when printing anagram list because its a character array.
#Space Complexity:: O(n) where n is the maximum number of elements.Using a hashmap and result array.
#Did this code successfully run on Leetcode : Yes
#Any problem you faced while coding this : No
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagramDict = {}
        result=[]
        
        for word in strs:
            key=sorted(word)
            key="".join(key)
            if key not in anagramDict:
                anagramDict[key]=[word]
            else:
                anagramDict[key].append(word)
                
        for k,v in anagramDict.items():
            result.append(v)
        
        return result