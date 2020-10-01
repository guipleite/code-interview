# https://leetcode.com/problems/jump-game/

def canJump( nums):

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
        
L2 = [3,2,1,0,4]
L = [2,3,1,1,4]

print(canJump(L))

print(canJump(L2))