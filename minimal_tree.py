# CTCI #4.2

def minimal_tree(nums):

	root_idx = len(nums)//2

	root = BinTree(nums[root_idx])

	root.left = minimal_tree(nums[:root_idx-1])
    root.right = minimal_tree(nums[root_idx+1:])

    return root
	
