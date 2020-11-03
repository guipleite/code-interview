# https://leetcode.com/problems/first-missing-positive/submissions/

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        if nums: 
          for i in range(1,len(nums)+2):
            if i not in nums:
                return(i)
        else:    
            return 1