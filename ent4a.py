class TreeNode:
    def __init__(self, value=None, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

def in_order_succ(node: TreeNode) -> TreeNode:

    if node is not None:
        if node.right is not None:
            buff = node.right
            
            while buff.left is not None:
                buff = buff.left

            return buff
            
        elif node.parent is not None:
            if node.parent.value < node.value:
                buff = node.parent

                while buff and buff.value < node.value:
                    buff = buff.parent

                return buff

            else:
                return node.parent
            
        else:
            return None

    else:
        return None
        