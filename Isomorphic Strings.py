#Time Complexity:: Average: O(n) - using for loop with range of array
#Space Complexity:: O(n) where n is the maximum number of elements.Using hashmap and hashset which consumes minimal space.
#Did this code successfully run on Leetcode : Yes
#Any problem you faced while coding this : No
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        hashmap={} #character mappings
        seen=set() #seen hashset
        
        for i in range(len(s)):
            if s[i] not in hashmap:
                if t[i] in seen:
                    return False
                hashmap[s[i]]=t[i]
                seen.add(t[i])
            else:
                if hashmap[s[i]]!=t[i]:
                    return False
        return True
