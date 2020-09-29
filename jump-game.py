# https://leetcode.com/problems/jump-game/

class Solution:
    def canJump(self, nums: List[int]) -> bool:
    
        if nums is  None:
            return False
        
        curr = len(nums) - 1
        i  = curr
        
        while i>=0:
            if nums[i] >= curr - i:
                curr = i
            
            i-=1

        if curr:
            return False
        else:
            return True
        