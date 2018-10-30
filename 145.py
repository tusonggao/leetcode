# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#后序遍历二叉树

class Solution:
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        else:
            return_list = self.postorderTraversal(root.left)
            return_list += self.postorderTraversal(root.right)
            return_list += [root.val]
            return return_list
        