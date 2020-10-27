# https://leetcode.com/problems/jump-game-ii/submissions/

class Solution:
    def jump(self, nums: List[int]) -> int:
        if nums is  None:
            return False

        curr = nums[0]
        iongest  = curr
        
        jmp = 1
        
        if len(nums) <= 1:
            jmp=0
 
        for i in range(1, len(nums)):
            if len(nums)-1 == i:
                return jmp

            if nums[i]+i > iongest:
                iongest = nums[i]+i
                
            if i >= curr:
                
                curr = iongest
                jmp+=1

        return jmp
        