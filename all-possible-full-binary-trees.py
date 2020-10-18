# https://leetcode.com/problems/all-possible-full-binary-trees/

class Solution:
    def allPossibleFBT(self, N: int) -> List[TreeNode]:

        trees = []
        
        for _ in range(N+1):
            trees.append([])

        trees[1].append(TreeNode(0))

        for r in range(1, N+1, 2):
            for l in range(1, r, 2):
                for node_l in trees[l]:
                    for node_r in trees[r-l-1]:
                        
                        root = TreeNode(0)
                        
                        root.left = node_l
                        root.right = node_r
                        
                        trees[r].append(root)
        
        return trees[N]