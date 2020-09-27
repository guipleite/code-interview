#https://leetcode.com/problems/path-sum-iii/submissions/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
        
    def DepthFirstSearch(self, root, sum):
        ans = 0
        
        if not root:
            return ans

        else:
        
            if root.val == sum:
                ans = 1
                
            ans += self.DepthFirstSearch(root.left,  sum - root.val)
            ans += self.DepthFirstSearch(root.right, sum - root.val)
            
        return ans
    
    def pathSum(self, root: 'TreeNode', sum: 'int') -> 'int':
        ans = 0

        if not root:
            return ans
        
        else:
            ans += self.DepthFirstSearch(root, sum) 
            ans += self.pathSum(root.left,  sum) 
            ans += self.pathSum(root.right, sum)
        
        return ans