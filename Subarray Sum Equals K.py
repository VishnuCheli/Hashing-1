#Time Complexity:: Average: TC-O(n) for  for loop as we traverse full array.
#Space Complexity:: O(1) -not using extra space and hashmap space complexity is almost O(1).
#Did this code successfully run on Leetcode : Yes
#Any problem you faced while coding this : No
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        rSumHashMap={0:1}
        
        count=0
        rSum=0
        
        for i in range(len(nums)):
            rSum+=nums[i]
            Compliment = rSum-k #K is the target sum of each subarray
            
            if Compliment in rSumHashMap:
                count+=rSumHashMap[Compliment]  #if compliment already in hashmap, increment count by number occurance          
            
            if rSum in rSumHashMap:
                rSumHashMap[rSum] += 1
            else:
                rSumHashMap[rSum] = 1
        return count