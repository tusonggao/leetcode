#递归解法

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetricEqualTree(self, root1, root2):
        if root1 is None and root2 is None:
            return True
        if root1 is None and root2 is not None:
            return False
        if root1 is not None and root2 is None:
            return False
        
        if root1.val != root2.val:
            return False
        
        return (self.isSymmetricEqualTree(root1.left, root2.right) and
                self.isSymmetricEqualTree(root1.right, root2.left))
        
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        return self.isSymmetricEqualTree(root.left, root.right)

		
#################################################################################

# 迭代解法









