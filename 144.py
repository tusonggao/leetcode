# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#前序遍历二叉树

class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        else:
            return_list = [root.val]
            return_list += self.preorderTraversal(root.left)
            return_list += self.preorderTraversal(root.right)
            return return_list