# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#中序遍历二叉树

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
		if root is None:
            return []
        else:
		    return_list = self.inorderTraversal(root.left)
            return_list += [root.val]
            return_list += self.inorderTraversal(root.right)
            return return_list