# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root is None:
            return False
        if root.val==sum and root.left==None and root.right==None:
            return True
        return (self.hasPathSum(root.left, sum-root.val) or 
                self.hasPathSum(root.right, sum-root.val))
        