# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        else:
            maxDepth_left = self.maxDepth(root.left)
            maxDepth_right = self.maxDepth(root.right)
            return max(maxDepth_left, maxDepth_right) + 1